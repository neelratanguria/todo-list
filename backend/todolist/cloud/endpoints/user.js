Parse.Cloud.define("v1_sign_up", async (request) => {
	const { email, password } = request.params;

    var userClass = Parse.Object.extend("User")
    var user = new userClass();

    user.set("username", email);
    user.set("password", password);
    // user.set("name", name);

    user = await user.save();
    var userString = JSON.stringify(user)
    var userJson = JSON.parse(userString)
    return {status: true, message: "Task saved", objectId: userJson.objectId}
});
