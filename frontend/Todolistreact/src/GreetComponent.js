import React from "react";
import { Text, Image, Button, View, TextInput } from 'react-native';


const GreetComponent = (props) => {
    const onButtonPress = () => {
        console.log("Hey sexy")
    }
    return (
        <View>
            <TextInput
                style={{ padding: 10, borderWidth: 1, marginHorizontal: 20, marginVertical: 10 }}
                placeholder={"Email"}
            />
            <TextInput
                style={{ padding: 10, borderWidth: 1, marginHorizontal: 20, marginVertical: 10 }}
                placeholder={"Password"}
            />
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