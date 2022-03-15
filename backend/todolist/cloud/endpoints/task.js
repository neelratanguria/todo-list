Parse.Cloud.define("v1_createTask", async (request) => {
	const { user_id, task_name, due_date } = request.params;

    var queryUser = new Parse.Query("User");
    var user = null;
    try {
        user = await queryUser.get(user_id);
    } catch(error) {
        return {success: false,
            message: "User not in database"}
    }
    

    var taskClass = Parse.Object.extend('Task')
    var task = new taskClass();

    task.set("user_pointer", user);
    task.set("task", task_name);
    task.set("due_date", due_date);

    await task.save();
    return {status: true, message: "Task saved"}
});

Parse.Cloud.define("v1_updateTask", async (request) => {
	const { task_id, task_name, due_date } = request.params;

    if(!task_id) {
        return {
            success: false,
            message: "'task_id' required"
        }
    }

    // Extend class
    var queryTask = new Parse.Query("Task");
    let task = await queryTask.get(task_id);

    

    // console.log(paper)
    // Set the input values to the new "User" object
    if(task_name) {
        task.set("task", task_name);
    }

    if(due_date) {
        task.set("due_date", due_date);
    }

    // Call the save method, which returns the saved object if successful
    task = await task.save();
    return {
        success: true,
        message: "Task updated"
    }
});

Parse.Cloud.define("v1_deletedTask", async (request) => {
	const { task_id } = request.params;

    if(!task_id) {
        return {
            success: false,
            message: "'task_id' required"
        }
    }

    // Extend class
    var queryTask = new Parse.Query("Task");
    let task = await queryTask.get(task_id);
    await task.destroy();
    return {
        success: true,
        message: "Task deleted"
    }
});

Parse.Cloud.define("v1_readTask", async (request) => {
	const { task_id } = request.params;

    if(!task_id) {
        return {
            success: false,
            message: "'task_id' required"
        }
    }

    // Extend class
    var queryTask = new Parse.Query("Task");
    queryTask.include("user_pointer")
    let task = await queryTask.get(task_id);
    return {
        success: true,
        message: "Task fetched",
        task: task
    }
});

Parse.Cloud.define("v1_fetchByUser", async (request) => {
    const { user_id } = request.params;

    if(!user_id) {
        return {
            success: false,
            message: "'user_id' required"
        }
    }

    const taskPointer = { __type: "Pointer", className: "_User", objectId: user_id }

	var query = new Parse.Query("Task");
    query.equalTo("user_pointer", taskPointer)
    query.include("user_pointer")
    let taskList = await query.find();

    return {
        success: true,
        message: "All tasks fetched",
        tasks: taskList
    }
});

Parse.Cloud.define("v1_fetchUsersIncompleteTask", (request) => {
	return "Hello world!";
});

Parse.Cloud.define("v1_markTaskComplete", async (request) => {
	const { task_id } = request.params;

    if(!task_id) {
        return {
            success: false,
            message: "'task_id' required"
        }
    }

    // Extend class
    var queryTask = new Parse.Query("Task");
    let task = await queryTask.get(task_id);

    // console.log(paper)
    // Set the input values to the new "User" object
    task.set("completion", true);

    // Call the save method, which returns the saved object if successful
    task = await task.save();
    return {
        success: true,
        message: "Task marked as done"
    }
});
