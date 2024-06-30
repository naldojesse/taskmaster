#!/usr/bin/env python3

"""
Dynamic File Tree Watcher

This script monitors a specified directory and updates a file with the directory tree structure whenever changes occur.
It uses the `watchdog` library to watch for file system events and logs activities.

Usage:
    python dynamic_file_tree_watcher.py -d <directory> -o <output_file> -s -f -l <log_file> -u

Arguments:
    -d, --directory       Specify directory to monitor (default is current directory).
    -o, --output          Output file to save the directory tree (default is repo_file_tree.txt).
    -s, --show-hidden     Show hidden files.
    -f, --follow-symlinks Follow symbolic links.
    -l, --log-file        Log file to store logs.
    -u, --update          Enable dynamic updates using watchdog.
"""

import os
import argparse
import logging
import pathspec

def setup_logging(log_file=None):
    """
    Set up logging configuration.

    Args:
        log_file (str, optional): Path to the log file. If not provided, logs will be printed to the console.
    """
    log_format = '%(asctime)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_format)
    if log_file:
        handler = logging.FileHandler(log_file)
        handler.setFormatter(logging.Formatter(log_format))
        logging.getLogger().addHandler(handler)

def load_gitignore(directory):
    """
    Load .gitignore file and return a pathspec matcher.

    Args:
        directory (str): The root directory to look for .gitignore.

    Returns:
        pathspec.PathSpec: A PathSpec object for matching ignored paths.
    """
    gitignore_path = os.path.join(directory, '.gitignore')
    if os.path.exists(gitignore_path):
        with open(gitignore_path, 'r') as f:
            gitignore_content = f.read()
        return pathspec.PathSpec.from_lines('gitwildmatch', gitignore_content.splitlines())
    return None

def print_directory_tree(directory, show_hidden=False, follow_symlinks=False, gitignore_spec=None):
    """
    Generate a directory tree structure.

    Args:
        directory (str): The root directory to generate the tree from.
        show_hidden (bool, optional): Whether to include hidden files. Defaults to False.
        follow_symlinks (bool, optional): Whether to follow symbolic links. Defaults to False.
        gitignore_spec (pathspec.PathSpec, optional): PathSpec object for matching ignored paths.

    Returns:
        list: A list of strings representing the directory tree.
    """
    tree = []

    def build_tree(current_path, current_indent):
        try:
            entries = sorted(os.listdir(current_path))
        except PermissionError:
            tree.append(f"{current_indent}[Permission Denied: {current_path}]")
            logging.error(f"Permission denied for directory: {current_path}")
            return
        
        entries = [e for e in entries if show_hidden or not e.startswith('.')]
        if gitignore_spec:
            entries = [e for e in entries if not gitignore_spec.match_file(os.path.join(current_path, e))]
        
        for count, entry in enumerate(entries):
            entry_path = os.path.join(current_path, entry)
            if count == len(entries) - 1:
                connector = "└──"
                new_indent = current_indent + "    "
            else:
                connector = "├──"
                new_indent = current_indent + "│   "

            if os.path.isdir(entry_path):
                tree.append(f"{current_indent}{connector} {entry}/")
                if follow_symlinks or not os.path.islink(entry_path):
                    build_tree(entry_path, new_indent)
            else:
                tree.append(f"{current_indent}{connector} {entry}")

    tree.append(directory)
    build_tree(directory, "")
    return tree

def save_tree_to_file(tree, output_file):
    """
    Save the directory tree to a file.

    Args:
        tree (list): The directory tree structure.
        output_file (str): The file to save the tree to.
    """
    try:
        with open(output_file, 'w') as f:
            for line in tree:
                f.write(line + '\n')
    except IOError as e:
        logging.error(f"Error writing to file {output_file}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Print directory tree to a file.')
    parser.add_argument('-d', '--directory', type=str, default='.', help='Specify directory to monitor (default is current directory).')
    parser.add_argument('-o', '--output', type=str, default='repo_file_tree.txt', help='Output file (default is repo_file_tree.txt).')
    parser.add_argument('-s', '--show-hidden', action='store_true', help='Show hidden files.')
    parser.add_argument('-f', '--follow-symlinks', action='store_true', help='Follow symbolic links.')
    parser.add_argument('-l', '--log-file', type=str, help='Log file to store logs.')
    parser.add_argument('-u', '--update', action='store_true', help='Enable dynamic updates using watchdog.')

    args = parser.parse_args()
    
    setup_logging(args.log_file)

    gitignore_spec = load_gitignore(args.directory)

    if args.update:
        from watchdog.observers import Observer
        from watchdog.events import FileSystemEventHandler

        class FileTreeHandler(FileSystemEventHandler):
            """
            Event handler for file system events to update the directory tree.

            Attributes:
                directory (str): The directory to monitor.
                output_file (str): The file to save the directory tree to.
                show_hidden (bool): Whether to include hidden files.
                follow_symlinks (bool): Whether to follow symbolic links.
                gitignore_spec (pathspec.PathSpec): PathSpec object for matching ignored paths.
            """
            def __init__(self, directory, output_file, show_hidden, follow_symlinks, gitignore_spec):
                self.directory = directory
                self.output_file = output_file
                self.show_hidden = show_hidden
                self.follow_symlinks = follow_symlinks
                self.gitignore_spec = gitignore_spec
                self.update_tree()

            def update_tree(self):
                """
                Update the directory tree and save it to the output file.
                """
                directory_tree = print_directory_tree(self.directory, self.show_hidden, self.follow_symlinks, self.gitignore_spec)
                save_tree_to_file(directory_tree, self.output_file)
                logging.info(f"File tree updated and saved to {self.output_file}")

            def on_any_event(self, event):
                """
                Handle any file system event.

                Args:
                    event (FileSystemEvent): The file system event.
                """
                if event.is_directory:
                    return
                self.update_tree()

            def on_created(self, event):
                """
                Handle file creation event.

                Args:
                    event (FileSystemEvent): The file system event.
                """
                logging.info(f"File created: {event.src_path}")
                self.update_tree()

            def on_deleted(self, event):
                """
                Handle file deletion event.

                Args:
                    event (FileSystemEvent): The file system event.
                """
                logging.info(f"File deleted: {event.src_path}")
                self.update_tree()

            def on_modified(self, event):
                """
                Handle file modification event.

                Args:
                    event (FileSystemEvent): The file system event.
                """
                logging.info(f"File modified: {event.src_path}")
                self.update_tree()

            def on_moved(self, event):
                """
                Handle file move event.

                Args:
                    event (FileSystemEvent): The file system event.
                """
                logging.info(f"File moved: from {event.src_path} to {event.dest_path}")
                self.update_tree()

        event_handler = FileTreeHandler(args.directory, args.output, args.show_hidden,
                                        args.follow_symlinks, gitignore_spec)
        observer = Observer()
        observer.schedule(event_handler, path=args.directory, recursive=True)
        
        try:
            logging.info(f"Starting directory watcher for {args.directory}")
            observer.start()
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
    else:
        directory_tree = print_directory_tree(args.directory, args.show_hidden, args.follow_symlinks, gitignore_spec)
        save_tree_to_file(directory_tree, args.output)
        logging.info(f"File tree generated and saved to {args.output}")