import React, { useEffect, useState } from "react";
import { Text, Image, Button, View, TextInput } from 'react-native';
import axios from "axios";

var mEmail
const onEmailType = (text) => {
    mEmail = text
}

var mPassword
const onPasswordType = (text) => {
    mPassword = text
}

const GreetComponent = (props) => {

    const [maskPasswordState, setMaskState] = useState(true)
    var maskPassword = false

    const onButtonPress = () => {
        console.log("creating user")
        axios.post("https://parseapi.back4app.com/users", {
            "username": mEmail,
            "password": mPassword
        }, {
            headers: {
                'X-Parse-Application-Id': '',
                'X-Parse-REST-API-Key': ''
            }
        }).then((res) => {
            console.log(res.status)
        }).catch((err) => {
            console.log(err)
        })
    }

    const onPassTogglePress = () => {
        console.log("view val toggled")
        if (maskPasswordState) {
            setMaskState(false)
        } else {
            setMaskState(true)
        }
    }
    return (
        <View>
            <TextInput
                style={{ padding: 10, borderWidth: 1, marginHorizontal: 20, marginVertical: 10 }}
                placeholder={"Email"}
                onChangeText={onEmailType}
            />
            <TextInput
                style={{ padding: 10, borderWidth: 1, marginHorizontal: 20, marginVertical: 10 }}
                placeholder={"Password"}
                onChangeText={onPasswordType}
                secureTextEntry={maskPasswordState}
            />
            <View style={{ margin: 20 }}>
                <Button
                    title={"Toggle Password view"}
                    onPress={onPassTogglePress}
                />
            </View>
            <View style={{ margin: 20 }}>
                <Button
                    title={props.buttonName}
                    onPress={onButtonPress}
                />
            </View>
        </View>
    )
}


export default GreetComponent