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

Parse.Cloud.define("v1_updateTask", (request) => {
	return "Hello world!";
});

Parse.Cloud.define("v1_deletedTask", (request) => {
	return "Hello world!";
});

Parse.Cloud.define("v1_readTask", (request) => {
	return "Hello world!";
});

Parse.Cloud.define("v1_fetchByUser", (request) => {
	return "Hello world!";
});

Parse.Cloud.define("v1_fetchUsersIncompleteTask", (request) => {
	return "Hello world!";
});

Parse.Cloud.define("v1_markTaskComplete", (request) => {
	return "Hello world!";
});
