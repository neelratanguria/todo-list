/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow strict-local
 */

import React from 'react';
import GreetComponent from './src/GreetComponent';
import {
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  useColorScheme,
  View,
  Image
} from 'react-native';

import {
  Colors,
  DebugInstructions,
  Header,
  LearnMoreLinks,
  ReloadInstructions,
} from 'react-native/Libraries/NewAppScreen';

const App = () => {
  const isDarkMode = useColorScheme() === 'dark';

  const backgroundStyle = {
    backgroundColor: isDarkMode ? Colors.darker : Colors.lighter,
  };

  return (
    <SafeAreaView style={backgroundStyle}>
      <StatusBar barStyle={isDarkMode ? 'light-content' : 'dark-content'} />
      <ScrollView
        contentInsetAdjustmentBehavior="automatic"
        style={backgroundStyle}>
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
      </ScrollView>
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
