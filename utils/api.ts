import * as FileSystem from "expo-file-system";

export const API_URL = "http://192.168.1.5:8000";

export async function uploadAudioAndGetText(uri: string): Promise<string> {
  const form = new FormData();
  form.append("file", {
    uri,
    name: "audio.wav",
    type: "audio/wav",
  } as any);

  const res = await fetch(`${API_URL}/stt/`, {
    method: "POST",
    body: form,
  });

  const data = await res.json();
  return data.text;
}

export async function getTTSUrl(text: string): Promise<string> {
  const res = await fetch(`${API_URL}/tts/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text }),
  });

  const data = await res.json();
  return `${API_URL}/${data.audio_url}`;
}
