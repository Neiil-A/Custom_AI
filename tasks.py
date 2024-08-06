def perform_task(task_name, description):
    return f"Task {task_name} completed. Description: {description}"

# Example usage
if __name__ == "__main__":
    task_name = "sample task"
    description = "This is a sample task to demonstrate task handling."
    print(perform_task(task_name, description))
