class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task = {'title': title, 'description': description, 'completed': False}
        self.tasks.append(task)
        print(f'Task "{title}" added successfully.')

    def mark_task_as_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['completed'] = True
            print(f'Task "{self.tasks[task_index]["title"]}" marked as completed.')
        else:
            print('Invalid task index.')

    def display_tasks(self):
        if not self.tasks:
            print('No tasks available.')
        else:
            print('Tasks:')
            for i, task in enumerate(self.tasks):
                status = 'Completed' if task['completed'] else 'Incomplete'
                print(f'{i}. Title: {task["title"]}, Description: {task["description"]}, Status: {status}')

    def run_task_manager(self):
        while True:
            print('\nTask Manager Menu:')
            print('1. Add a Task')
            print('2. Mark Task as Completed')
            print('3. Display Tasks')
            print('4. Exit')
            choice = input('Enter your choice: ')

            if choice == '1':
                title = input('Enter task title: ')
                description = input('Enter task description: ')
                self.add_task(title, description)
            elif choice == '2':
                task_index = int(input('Enter the index of the task to mark as completed: '))
                self.mark_task_as_completed(task_index)
            elif choice == '3':
                self.display_tasks()
            elif choice == '4':
                print('Exiting Task Manager.')
                break
            else:
                print('Invalid choice. Please select a valid option.')

if __name__ == '__main__':
    task_manager = TaskManager()
    task_manager.run_task_manager()
