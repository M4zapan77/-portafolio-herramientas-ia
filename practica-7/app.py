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
    probabilidades = modelo(**entradas).logits[0].softmax(dim=0)
    valores, indices = probabilidades.topk(3)
    return {
        modelo.config.id2label[indice]: probabilidad
        for indice, probabilidad in zip(indices.tolist(), valores.tolist())
    }


if __name__ == "__main__":
    app = gr.Interface(
        fn=clasificar,
        inputs=gr.Image(type="pil", image_mode="RGB", label="Imagen"),
        outputs=gr.Label(num_top_classes=3, label="Predicciones"),
        title="Clasificador de imágenes",
    )
    app.launch()
