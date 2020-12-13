import React, { useState, useEffect } from 'react';
import { Text, View, StyleSheet, Button, Alert } from 'react-native';
import { BarCodeScanner } from 'expo-barcode-scanner';
import axios from 'axios';


export default function ScanQR() {
  const [hasPermission, setHasPermission] = useState(null);
  const [scanned, setScanned] = useState(false);

  useEffect(() => {
    (async () => {
      const { status } = await BarCodeScanner.requestPermissionsAsync();
      setHasPermission(status === 'granted');
    })();
  }, []);

  const sendToEvLoader = (token_amount, user_email) => {
    var config = {
      method: 'post',
      url: 'https://sup.evloader.com/api/wallet/sup-points',
      headers: { 
        'Content-Type': 'application/json'
      },
      data: {
        user_email,
        token_amount
      }
    };

    axios(config)
    .then(function (response) {
      console.log(JSON.stringify(response.data));
    })
    .catch(function (error) {
      console.log(error);
    });
  }

  const handleBarCodeScanned = ({ type, data }) => {
    setScanned(true);
    const token_amount = 20
    const user_email = "email@example.com"
    Alert.alert(
      `Κερδίσατε ${token_amount} πόντους`,
      "Μπορείτε να χρησιμοποιήσετε τους πόντους σε επόμενη αγορά, οικολογικών προϊόντων ή να φορτίσετε το ηλεκτρικό σας όχημα μέσω του EV Loader",
      [
        {
          text: "Ακύρωση",
          onPress: () => console.log("Cancel Pressed"),
          style: "cancel"
        },
        { text: "Εξαργύρωση στο EV Loader", onPress: () => sendToEvLoader(token_amount, user_email) }
      ],
      { cancelable: false }
    );
  };

  if (hasPermission === null) {
    return <Text>Requesting for camera permission</Text>;
  }
  if (hasPermission === false) {
    return <Text>No access to camera</Text>;
  }

  return (
    <View style={styles.container}>
      <BarCodeScanner
        onBarCodeScanned={scanned ? undefined : handleBarCodeScanned}
        style={StyleSheet.absoluteFillObject}
      />
      {scanned && <Button title={'Tap to Scan Again'} onPress={() => setScanned(false)} />}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    flexDirection: 'column',
    justifyContent: 'center',
  },
});