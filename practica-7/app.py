from pathlib import Path
from time import perf_counter

import gradio as gr
import torch
from transformers import AutoImageProcessor, AutoModelForImageClassification


MODELO = "google/mobilenet_v2_1.0_224"
procesador = AutoImageProcessor.from_pretrained(MODELO, backend="pil")
modelo = AutoModelForImageClassification.from_pretrained(MODELO)
modelo.eval()


@torch.inference_mode()
def clasificar(imagen):
    if imagen is None:
        raise gr.Error("Sube una imagen para clasificarla.")

    entradas = procesador(images=imagen, return_tensors="pt")
    inicio = perf_counter()
    logits = modelo(**entradas).logits
    segundos = perf_counter() - inicio

    probabilidades = logits[0].softmax(dim=0)
    valores, indices = probabilidades.topk(3)
    etiquetas = {
        modelo.config.id2label[indice]: probabilidad
        for indice, probabilidad in zip(indices.tolist(), valores.tolist())
    }
    return etiquetas, f"{segundos:.2f} s"


if __name__ == "__main__":
    carpeta_ejemplos = Path(__file__).resolve().parent / "ejemplos"
    ejemplos = [
        [str(archivo)]
        for archivo in sorted(carpeta_ejemplos.iterdir())
        if archivo.is_file() and archivo.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"}
    ]
    app = gr.Interface(
        fn=clasificar,
        inputs=gr.Image(type="pil", image_mode="RGB", label="Imagen"),
        outputs=[
            gr.Label(num_top_classes=3, label="Predicciones"),
            gr.Textbox(label="Tiempo del modelo en CPU", interactive=False),
        ],
        title="¿Qué hay en la foto?",
        description="El modelo MobileNet V2 (google/mobilenet_v2_1.0_224) clasifica la imagen.",
        examples=ejemplos,
        cache_examples=True,
        cache_mode="lazy",
    )
    app.launch()
