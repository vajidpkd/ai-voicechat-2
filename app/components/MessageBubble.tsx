import { View, Text } from "react-native";

export default function MessageBubble({
  text,
  sender,
}: {
  text: string;
  sender: "user" | "bot";
}) {
  return (
    <View
      style={{
        padding: 12,
        marginVertical: 6,
        backgroundColor: sender === "user" ? "#2563EB" : "#1F2937",
        alignSelf: sender === "user" ? "flex-end" : "flex-start",
        borderRadius: 12,
        maxWidth: "80%",
      }}
    >
      <Text style={{ color: "white" }}>{text}</Text>
    </View>
  );
}
