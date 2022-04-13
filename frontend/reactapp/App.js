/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow strict-local
 */

import React from 'react';
import {
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  useColorScheme,
  View,
  Image,
  Alert,
} from 'react-native';
import GreetComponent from './src/GreetComponent';


const App = () => {
  const isDarkMode = useColorScheme() === 'dark';

  return (
    <SafeAreaView>
      <StatusBar barStyle={isDarkMode ? 'light-content' : 'dark-content'} />

      <View style={{ alignItems: 'stretch', justifyContent: 'center', height: "100%" }}>
        <Text style={{ textAlign: "center", fontSize: 40 }}>Todo List</Text>
        <View style={{alignItems: "center", borderWidth: 2, marginHorizontal: 125}}>
          <Image
            style={styles.logo}
            source={require('./assets/newproduct.png')}
          />
        </View>
        <GreetComponent buttonName="Sign Up"
        />
      </View>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {},
  content: {
    alignItems: 'center',
    flex: 1,
    justifyContent: 'center'
  },
  form: {
    width: '100%'
  },
  item: {},
  logo: {
    justifyContent: 'center',
    alignItems: 'center',
    width: 100,
    height: 100,
    margin: 10,
    
  },
});

export default App;
