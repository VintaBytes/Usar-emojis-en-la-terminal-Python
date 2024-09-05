# Usar emojis en la terminal con Python
¿Cómo puedes usar emojis en la terminal Python? ¡En este repositorio te cuento como hacerlo!

En Python, puedes usar emojis o iconos en la terminal utilizando los caracteres Unicode que representan esos emojis. Esto es bastante sencillo y funciona en muchas terminales modernas que soportan la codificación UTF-8.
 
Puedes usar estos códigos Unicode en Python de la siguiente forma:

```python
print("Cara feliz: \U0001F600")
print("Cara con lágrimas de risa: \U0001F602")
print("Cara pensando: \U0001F914")
```

Esto mostrará los emojis correspondientes en la terminal, siempre y cuando la terminal soporte caracteres Unicode.

### Aquí tienes una lista de los emojis más comunes relacionados con caras, junto con sus códigos Unicode:

| Emoji | Descripción                       | Código Unicode |
|-------|-----------------------------------|----------------|
| 😀    | Cara sonriendo                    | `\U0001F600`   |
| 😁    | Cara sonriente con ojos grandes   | `\U0001F601`   |
| 😂    | Cara con lágrimas de risa         | `\U0001F602`   |
| 😃    | Cara sonriente con ojos grandes   | `\U0001F603`   |
| 😄    | Cara sonriente con ojos sonrientes| `\U0001F604`   |
| 😅    | Cara sonriente con sudor          | `\U0001F605`   |
| 😆    | Cara sonriente con ojos cerrados  | `\U0001F606`   |
| 😉    | Cara guiñando un ojo              | `\U0001F609`   |
| 😊    | Cara sonriente con ojos sonrientes| `\U0001F60A`   |
| 😋    | Cara saboreando comida            | `\U0001F60B`   |
| 😎    | Cara con gafas de sol             | `\U0001F60E`   |
| 😍    | Cara con ojos de corazón          | `\U0001F60D`   |
| 😘    | Cara lanzando un beso             | `\U0001F618`   |
| 😗    | Cara besando                      | `\U0001F617`   |
| 😙    | Cara besando con ojos cerrados    | `\U0001F619`   |
| 😚    | Cara besando con ojos sonrientes  | `\U0001F61A`   |
| 🤗    | Cara abrazando                    | `\U0001F917`   |
| 🤔    | Cara pensando                     | `\U0001F914`   |
| 🤨    | Cara arqueando una ceja           | `\U0001F928`   |
| 😐    | Cara neutral                      | `\U0001F610`   |
| 😑    | Cara sin expresión                | `\U0001F611`   |
| 😶    | Cara sin boca                     | `\U0001F636`   |
| 🙄    | Cara con ojos en blanco           | `\U0001F644`   |
| 😏    | Cara con sonrisa de lado          | `\U0001F60F`   |
| 😣    | Cara de desesperación             | `\U0001F623`   |
| 😥    | Cara triste pero aliviada         | `\U0001F625`   |
| 😮    | Cara sorprendida                  | `\U0001F62E`   |
| 🤐    | Cara con la boca cerrada con cremallera | `\U0001F910` |
| 😯    | Cara con la boca abierta          | `\U0001F62F`   |
| 😪    | Cara somnolienta                  | `\U0001F62A`   |
| 😫    | Cara cansada                      | `\U0001F62B`   |
| 😴    | Cara dormida                      | `\U0001F634`   |
| 😌    | Cara aliviada                     | `\U0001F60C`   |
| 😛    | Cara sacando la lengua            | `\U0001F61B`   |
| 😜    | Cara guiñando y sacando la lengua | `\U0001F61C`   |
| 😝    | Cara con los ojos cerrados y lengua fuera | `\U0001F61D`|
| 🤤    | Cara babeando                     | `\U0001F924`   |
| 😒    | Cara de desdén                    | `\U0001F612`   |
| 😓    | Cara con sudor frío               | `\U0001F613`   |
| 😔    | Cara pensativa                    | `\U0001F614`   |
| 😕    | Cara de confusión                 | `\U0001F615`   |
| 🙃    | Cara al revés                     | `\U0001F643`   |
| 🤑    | Cara con signo de dinero en los ojos | `\U0001F911`  |
| 😲    | Cara asombrada                    | `\U0001F632`   |
| ☹️    | Cara de tristeza                  | `\u2639`       |
| 🙁    | Cara de leve tristeza             | `\U0001F641`   |
| 😖    | Cara angustiada                   | `\U0001F616`   |
| 😞    | Cara decepcionada                 | `\U0001F61E`   |
| 😟    | Cara preocupada                   | `\U0001F61F`   |
| 😤    | Cara con la nariz resoplando      | `\U0001F624`   |
| 😢    | Cara llorando                     | `\U0001F622`   |
| 😭    | Cara llorando a mares             | `\U0001F62D`   |
| 😦    | Cara de tristeza con la boca abierta | `\U0001F626` |
| 😧    | Cara de angustia                  | `\U0001F627`   |
| 😨    | Cara aterrada                     | `\U0001F628`   |
| 😩    | Cara de agotamiento               | `\U0001F629`   |
| 🤯    | Cabeza explotando                 | `\U0001F92F`   |
| 😬    | Cara mostrando los dientes        | `\U0001F62C`   |
| 😰    | Cara con sudor frío               | `\U0001F630`   |
| 😱    | Cara gritando de miedo            | `\U0001F631`   |
| 😳    | Cara ruborizada                   | `\U0001F633`   |
| 🤪    | Cara de locura                    | `\U0001F92A`   |
| 😵    | Cara con los ojos en espiral      | `\U0001F635`   |
| 🤕    | Cara con venda en la cabeza       | `\U0001F915`   |
| 🤢    | Cara con náuseas                  | `\U0001F922`   |
| 🤮    | Cara vomitando                    | `\U0001F92E`   |
| 🤧    | Cara estornudando                 | `\U0001F927`   |
| 😇    | Cara con halo                     | `\U0001F607`   |
| 🥳    | Cara de fiesta                    | `\U0001F973`   |


### Aquí tienes una lista de los códigos Unicode de algunos de los emojis más comunes relacionados con la comida:

| Emoji | Descripción          | Código Unicode |
|-------|----------------------|----------------|
| 🍏    | Manzana verde         | `\U0001F34F`   |
| 🍎    | Manzana roja          | `\U0001F34E`   |
| 🍐    | Pera                 | `\U0001F350`   |
| 🍊    | Naranja              | `\U0001F34A`   |
| 🍋    | Limón                | `\U0001F34B`   |
| 🍌    | Banana               | `\U0001F34C`   |
| 🍉    | Sandía               | `\U0001F349`   |
| 🍇    | Uvas                 | `\U0001F347`   |
| 🍓    | Fresa                | `\U0001F353`   |
| 🍒    | Cerezas              | `\U0001F352`   |
| 🍑    | Durazno              | `\U0001F351`   |
| 🥝    | Kiwi                 | `\U0001F95D`   |
| 🍍    | Piña                 | `\U0001F34D`   |
| 🥭    | Mango                | `\U0001F96D`   |
| 🥥    | Coco                 | `\U0001F965`   |
| 🥑    | Aguacate             | `\U0001F951`   |
| 🍅    | Tomate               | `\U0001F345`   |
| 🥕    | Zanahoria            | `\U0001F955`   |
| 🌽    | Mazorca de maíz       | `\U0001F33D`   |
| 🍆    | Berenjena            | `\U0001F346`   |
| 🥒    | Pepino               | `\U0001F952`   |
| 🥬    | Hoja de verdura      | `\U0001F96C`   |
| 🥔    | Papa                 | `\U0001F954`   |
| 🥖    | Baguette             | `\U0001F956`   |
| 🥐    | Croissant            | `\U0001F950`   |
| 🍞    | Pan                  | `\U0001F35E`   |
| 🧀    | Queso                | `\U0001F9C0`   |
| 🍗    | Pollo asado          | `\U0001F357`   |
| 🍖    | Carne con hueso      | `\U0001F356`   |
| 🍔    | Hamburguesa          | `\U0001F354`   |
| 🍟    | Papas fritas         | `\U0001F35F`   |
| 🍕    | Pizza                | `\U0001F355`   |
| 🌭    | Hotdog               | `\U0001F32D`   |
| 🍿    | Palomitas de maíz     | `\U0001F37F`   |
| 🥓    | Tocino               | `\U0001F953`   |
| 🥚    | Huevo                | `\U0001F95A`   |
| 🍳    | Huevo frito          | `\U0001F373`   |
| 🥞    | Panqueques           | `\U0001F95E`   |
| 🍝    | Espagueti            | `\U0001F35D`   |
| 🍲    | Tazón de sopa        | `\U0001F372`   |
| 🍣    | Sushi                | `\U0001F363`   |
| 🍤    | Camarón frito        | `\U0001F364`   |
| 🍪    | Galleta              | `\U0001F36A`   |
| 🍩    | Dona                 | `\U0001F369`   |
| 🍫    | Barra de chocolate   | `\U0001F36B`   |
| 🍰    | Pastel               | `\U0001F370`   |
| 🎂    | Torta de cumpleaños  | `\U0001F382`   |
| 🍧    | Raspado              | `\U0001F367`   |
| 🍨    | Helado               | `\U0001F368`   |
| 🍦    | Cono de helado       | `\U0001F366`   |
| 🍯    | Tarro de miel        | `\U0001F36F`   |
| 🍼    | Biberón              | `\U0001F37C`   |
| 🥤    | Vaso con popote      | `\U0001F964`   |
| 🍵    | Té caliente          | `\U0001F375`   |
| 🍺    | Cerveza              | `\U0001F37A`   |


