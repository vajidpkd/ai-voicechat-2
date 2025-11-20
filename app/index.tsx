import { View, Text, TouchableOpacity } from "react-native";
import { Link } from "expo-router";

export default function Home() {
  return (
    <View style={{ flex: 1, justifyContent: "center", alignItems: "center" }}>
      <Text style={{ fontSize: 26, marginBottom: 20 }}>🔊 AI Voice Assistant</Text>

      <Link href="/voice" asChild>
        <TouchableOpacity
          style={{
            backgroundColor: "#4F46E5",
            padding: 15,
            borderRadius: 10,
          }}
        >
          <Text style={{ color: "white", fontSize: 18 }}>Start Voice Assistant</Text>
        </TouchableOpacity>
      </Link>

      <Link href="/settings" asChild>
        <TouchableOpacity
          style={{
            marginTop: 15,
            backgroundColor: "#6B7280",
            padding: 15,
            borderRadius: 10,
          }}
        >
          <Text style={{ color: "white", fontSize: 18 }}>Settings</Text>
        </TouchableOpacity>
      </Link>
    </View>
  );
}
