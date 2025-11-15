# setup_environment.py
import nltk

def download_nltk_resources():
    """Descarga los recursos necesarios de NLTK"""
    resources = [
        'stopwords',
        'averaged_perceptron_tagger', 
        'wordnet',
        'punkt'
    ]
    
    for resource in resources:
        try:
            nltk.download(resource)
            print(f"✓ {resource} descargado correctamente")
        except Exception as e:
            print(f"✗ Error descargando {resource}: {e}")

if __name__ == "__main__":
    download_nltk_resources()
    print("Configuración del entorno completada.")