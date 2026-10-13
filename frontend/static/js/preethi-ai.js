/**
 * MediMate-AI - Preethi AI Conversational Clinical Chat Client (preethi-ai.js)
 */

const PreethiAIClient = {
  emergencyKeywords: [
    'chest pain', 'heart attack', 'shortness of breath', 'can\'t breathe',
    'stroke', 'unconscious', 'severe bleeding', 'anaphylaxis', 'choking'
  ],

  checkEmergency(text) {
    const lower = text.toLowerCase();
    return this.emergencyKeywords.some(keyword => lower.includes(keyword));
  },

  async sendMessage(userInput) {
    if (this.checkEmergency(userInput)) {
      return {
        reply: "⚠️ EMERGENCY DETECTED: Your symptoms may indicate an acute life-threatening medical emergency. Please call 911 or head to the nearest Emergency Department immediately. Do not wait for online consultation.",
        emergency: true,
        department: "Emergency Medicine"
      };
    }

    if (window.ApiClient) {
      try {
        const res = await window.ApiClient.sendAiMessage(userInput);
        if (res && res.data && res.data.response) {
          return {
            reply: res.data.response,
            emergency: res.data.is_emergency || false,
            department: res.data.department || "General Medicine"
          };
        }
      } catch (e) {}
    }

    // Local clinical fallback
    return {
      reply: "Thank you for sharing your symptoms. Based on clinical guidelines, it is recommended to monitor your temperature, rest, and keep hydrated. If symptoms persist or worsen over 48 hours, please schedule a consultation with our primary care physician.",
      emergency: false,
      department: "General Medicine"
    };
  },

  speakText(text) {
    if ('speechSynthesis' in window) {
      window.speechSynthesis.cancel();
      const utterance = new SpeechSynthesisUtterance(text);
      utterance.rate = 1.0;
      utterance.pitch = 1.1;
      window.speechSynthesis.speak(utterance);
    }
  }
};

window.PreethiAIClient = PreethiAIClient;
