import { useState } from "react";
import { View, Text, ScrollView } from "react-native";
import AudioButton from "./components/AudioButton";
import MessageBubble from "./components/MessageBubble";
import { uploadAudioAndGetText, getTTSUrl } from "../utils/api";

export default function VoiceScreen() {
  const [messages, setMessages] = useState<{ text: string; sender: "user" | "bot" }[]>([]);

  const handleResult = async (uri: string) => {
    const text = await uploadAudioAndGetText(uri);

    setMessages((prev) => [...prev, { text, sender: "user" }]);

    const audioUrl = await getTTSUrl(text);

    setMessages((prev) => [
      ...prev,
      { text: `🔊 Playing audio: ${audioUrl}`, sender: "bot" },
    ]);
  };

  return (
    <View style={{ flex: 1, paddingTop: 50 }}>
      <ScrollView style={{ padding: 15 }}>
        {messages.map((msg, index) => (
          <MessageBubble key={index} text={msg.text} sender={msg.sender} />
        ))}
      </ScrollView>

      <AudioButton onRecorded={handleResult} />
    </View>
  );
}
