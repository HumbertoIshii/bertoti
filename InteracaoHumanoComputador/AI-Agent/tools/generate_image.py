from smolagents import tool
from craiyon import Craiyon
import os

@tool
class GenerateImageTool:
    """
    Ferramenta que gera uma imagem a partir de um prompt textual usando o Craiyon (DALL·E Mini).
    """

    name: str = "generate_image"
    description: str = "Gera uma imagem a partir de uma descrição em texto usando Craiyon (DALL·E Mini)."

    def __init__(self):
        # Inicializando o Craiyon
        self.craiyon = Craiyon()

    def __call__(self, prompt: str) -> str:
        """
        Gera uma imagem a partir de uma descrição textual usando o Craiyon.

        Args:
            prompt (str): Uma descrição em linguagem natural da imagem desejada.

        Returns:
            str: Caminho do arquivo da imagem gerada.
        """
        try:
            # Gerando a imagem com o Craiyon
            result = self.craiyon.draw(prompt)

            # Criando o diretório para salvar a imagem, caso não exista
            os.makedirs("generated_images", exist_ok=True)

            # Definindo o caminho da imagem gerada
            image_path = f"generated_images/image_{abs(hash(prompt)) % (10 ** 8)}.png"
            result.save(image_path)

            return f"Imagem gerada com sucesso: {image_path}"
        except Exception as e:
            return f"Erro ao gerar imagem: {str(e)}"
