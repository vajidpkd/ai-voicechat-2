import { TouchableOpacity, Text } from "react-native";
import useRecorder from "../../hooks/useRecorder";

export default function AudioButton({ onRecorded }: { onRecorded: (uri: string) => void }) {
  const { recording, startRecording, stopRecording } = useRecorder(onRecorded);

  return (
    <TouchableOpacity
      onPress={recording ? stopRecording : startRecording}
      style={{
        backgroundColor: recording ? "#DC2626" : "#16A34A",
        padding: 18,
        margin: 15,
        borderRadius: 50,
        alignItems: "center",
      }}
    >
      <Text style={{ color: "white", fontSize: 20 }}>
        {recording ? "Stop Recording" : "Start Recording"}
      </Text>
    </TouchableOpacity>
  );
}
