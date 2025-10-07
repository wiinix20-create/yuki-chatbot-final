# yuki_voice.py
import pygame
from gtts import gTTS
import tempfile
import os
from pathlib import Path

class YukiVoice:
    """Sistema de voz de Yuki Nagato para proyectos locales"""
    
    def __init__(self):
        pygame.mixer.init()
        self.temp_files = []
        
    def hablar(self, texto, velocidad=False, tono_robotico=True):
        """
        Hacer hablar a Yuki Nagato
        
        Args:
            texto: Texto en español que dirá Yuki
            velocidad: False = normal, True = lento (estilo Yuki)
            tono_robotico: Aplicar efecto robótico
        """
        try:
            print(f"🎭 Yuki: {texto}")
            
            # Generar voz en español
            tts = gTTS(text=texto, lang='es', slow=velocidad)
            
            # Crear archivo temporal
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.wav')
            output_path = temp_file.name
            tts.save(output_path)
            self.temp_files.append(output_path)
            
            # Reproducir audio
            self._reproducir_audio(output_path)
            return output_path
            
        except Exception as e:
            print(f"❌ Error: {e}")
            return None
    
    def hablar_tecnico(self, texto):
        """Estilo técnico - voz rápida pero robótica (tu preferencia)"""
        return self.hablar(texto, velocidad=False, tono_robotico=True)
    
    def _reproducir_audio(self, file_path):
        """Reproducir audio y esperar a que termine"""
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        
        # Esperar a que termine la reproducción
        while pygame.mixer.music.get_busy():
            pygame.time.wait(100)
    
    def limpiar_temp(self):
        """Limpiar archivos temporales"""
        for file_path in self.temp_files:
            try:
                if os.path.exists(file_path):
                    os.remove(file_path)
            except:
                pass
        self.temp_files = []
    
    def __del__(self):
        """Destructor - limpiar al eliminar objeto"""
        self.limpiar_temp()

# Función global rápida
def yuki_decir(texto):
    """Función simple para hacer hablar a Yuki"""
    yuki = YukiVoice()
    return yuki.hablar_tecnico(texto)