from model_path import MODEL_PATH
import llama_cpp
import Personnage

class MaitreDeJeu:
    base_contexte = """ You must strictly stay within the context of elements provided in each prompt.
        Never more than 3 sentences. Don't go beyond that. Speak english and not another language.
        You are a Game Master for a text-based RPG. You must:
- Strictly stay within the context of elements provided in each prompt
- Use an epic and immersive tone
- Never invent new characters, objects or locations
- Only describe what is explicitly mentioned
- Use medieval-fantasy vocabulary
- Keep descriptions concise but vivid

Response format:
- Atmospheric descriptions in 50-100 words maximum
- No dialogues unless specifically requested
- No addition of narrative elements not provided"""

    def nouvelle_salle(self, ennemis, objets):
        elements = {
            "enemies": [e.nom for e in ennemis] if ennemis else ["no enemy"],
            "objects": [o.nom for o in objets] if objets else ["no object"]
        }
        prompt = f"Room containing: {', '.join(elements['enemies'])} and {', '.join(elements['objects'])}"
        a.InvokeModel(prompt)

    def donne_sorties(self, sorties):
        prompt = f"Tell the RPG player the room exits are {', '.join(sorties)} in no more than 50 words."
        a.InvokeModel(prompt)

    def attaque(self, attaquant, status, victime, degats, heroAttaque):
        if degats == "0":
            degats = "no"
        if heroAttaque:
            prompt = f"Describe {attaquant} who {status} a {victime} dealing {degats} damage points in no more than 50 words."
        else:
            prompt = f"Describe a {attaquant} who {status} {victime} dealing {degats} damage points in no more than 50 words."
        a.InvokeModel(prompt)

    def invoke_limit(prompt):
        a.InvokeModel(prompt + ". Tell this in no more than 50 words.")

    def invoke_marchand(self):
        prompt = "You are an RPG merchant. Make a small sinister speech to introduce yourself"
        a.InvokeModel(prompt)

    def InvokeModel(self,
                    prompt
                    ):
        model = llama_cpp.Llama(

            model_path = MODEL_PATH, # créer un fichier model_path.py et y mettre le chemin du modèle tel que MODEL_PATH = "D:\\Downloads\\Qwen2.5-7B-Instruct-Q3_K_S.gguf" (exemple)
                                     # ajouter src/model_path.py dans le .gitignore

                               
            # evite d'afficher toutes les informations de debug.
            stream = False,
            verbose = False,
            n_ctx= 2048, # pour 7B 
            n_threads=4
            # n_ctx= 8192 # pour 5B 

        )
        
        messages = [{"role": "system", "content": MaitreDeJeu.base_contexte},
                    {"role": "user", "content": prompt}]
        response = model.create_chat_completion(messages=messages,
            # taille maximum de la reponse
            max_tokens = 100,
            temperature= 0.7,
            # utilisé pour stopper la generation de texte à un caractere    
            # ou chaine de caractere ex: stop = [".", "?"]
            stop = ["<|endoftext|>","###"],
            top_p= 0.95,
            repeat_penalty=1.1
            )['choices'][0]["message"]["content"]
        print(response)
        


a = MaitreDeJeu()
# a.InvokeModel("Décris une salle de donjon RPG. Le joueur entre dans une salle sombre, contenant deux goblins, un ogre, et une potion magique. Utilise moins de 100 mots.")
# a.nouvelle_salle(["a goblin", "a goblin"], ["a potion"])
# a.attaque("dragon", "attaque", "le joueur", "15", False)
# a.donne_sorties(["est"])
# a.invoke_marchand()
# a.InvokeModel(base_context, "You are an RPG merchant. Make a small sinister speech to introduce yourself")