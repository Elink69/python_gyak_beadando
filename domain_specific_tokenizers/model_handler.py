"""
    A modelleket és múveleteiket kezelő osztály
"""

from transformers import BertTokenizerFast, BertForSequenceClassification, \
     BertConfig
import torch
import numpy as np
from domain_specific_tokenizers import read_config


class TrainedModel():
    """
        A modelleket és a hozzájuk tartozó művelteket kezelő osztály
    """

    def __init__(self, tokenizer: str, model: str) -> None:

        config = read_config.read_config()
        token = config["HuggingFaceToken"]
        id2label = {int(k): v for k, v in config["id2label"].items()}
        label2id = config["label2id"]

        self.tokenizer = BertTokenizerFast.\
            from_pretrained(f"VargaD/{tokenizer}_bert", token=token)

        self.config = BertConfig.from_pretrained(f"VargaD/{model}_bert",
                                                 num_labels=2,
                                                 id2label=id2label,
                                                 label2id=label2id,
                                                 token=token)

        self.model = BertForSequenceClassification.\
            from_pretrained(f"VargaD/{model}_bert",
                            config=self.config,
                            token=token)

        if torch.cuda.is_available():
            model.cuda()

    def tokenize_input(self, text: str) -> torch.Tensor:
        """
            A megadott szöveg tokenizálását végző függvény

            returns: Tokenizált szöveg torch Tensor-ként
        """

        return self.tokenizer(text,
                              padding='max_length',
                              max_length=128,
                              truncation=True,
                              return_tensors='pt')

    def rate_input(self, tokenized_input: torch.Tensor) -> str:
        """
            A szöveg kiértékelését végző függvény
        """
        self.model.eval()
        tokenized_input.to(self.model.device)
        logits = self.model(**tokenized_input, return_dict=True).\
            logits.detach().cpu().numpy()
        return self.model.config.id2label[np.argmax(logits, axis=1)[0]]
