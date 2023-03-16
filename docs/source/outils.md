# Les outils

## Comment faire une présentation avec Xaringan ?

### Objectifs

xaringan permet de produire des slides au format HTML, qui s'affichent dans le navigateur. Ces slides sont publiées sur le web et contribuent au bon référencement de nos contenus et à la diffusion de notre expertise. Comme de nombreuses productions de Datactivist, elles sont idéalement réutilisables en licence Creative Commons BY-SA.

Autre avantage : on peut y intégrer des figures produites directement avec du code R (programmation lettrée), des frames HTML (vidéo YouTube, tweet, contenu interactif genially…), des tableaux interactifs (package DT : exemple)…

### Installer xaringan

1. installer le logiciel RStudio Desktop
2. pour installer le template (qui installe la dépendance xaringan), lancer la commande :

   `remotes::install_github("datactivist/slides_datactivist")`

   Si remotes n'est pas installé, il faut aller dans la fenêtre Packages > Install et taper 'remotes' pour installer le package (ou exécuter la commande `install.packages('remotes')`).
3. redémarrer RStudio.

### Créer et modifier une présentation

Une fois l'installation effectuée, créer une nouvelle présentation dans Rstudio avec le menu File > New File > R Markdown..

Dans la boite de dialogue, choisir From Template > Slides Datactivist :

Il est aussi possible d'ouvrir une présentation Rmd existante dans RStudio pour la modifier.

La présentation se présente sous la forme d'un header yaml (séparé entre '---') qui gère les paramètres de compilation, et de texte brut mêlant le contenu des diapos et les instructions de mise en forme.

La syntaxe de la mise en page de la préz est décrite ici (en anglais) : https://bookdown.org/yihui/rmarkdown/xaringan-format.html

La syntaxe Markdown permettant d'ajouter et mettre en forme du texte est ici (en anglais) : https://bookdown.org/yihui/rmarkdown/markdown-syntax.html

xaringan n'est pas WYSIWYG (What you see is what you get) : vous ne voyez pas la forme définitive de la préz quand vous l'éditez. Pour cela, il est possible de lancer le prévisualiseur en cliquant dans RStudio sur Addins > Slides Datactivist ou bien Addins > Infinite Moon Reader. A chaque fois que vous enregistrerez votre fichier Rmd, le prévisualiseur se rafraîchira. Attention : Infinite Moon Reader n'est pas parfait et, dans certains cas, peut échouer à prévisualiser certains contenus.

### Ajouter des images

Chaque image doit être doit accessible sur le web (attention aux questions de droit et au fait que les images peuvent disparaître), ou mieux enregistrée sur votre ordinateur dans un répertoire (par exemple /img) placé dans le même dossier que la préz Rmd.

La syntaxe est la suivante :

```markdown
.center[.reduite[![](img/monimage.png)]]
.center[![:largeur 70%](img/monimage.png)]
.pull-right[.reduite3[![](img/monimage.png)]
.pull-left[.reduite2[![](img/monimage.png)]
