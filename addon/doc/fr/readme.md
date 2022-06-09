# Manuel de cricricri pour NVDA

Petite extension qui nous aidera à changer la date des manifestes.

Maintenant, selon la dernière politique de NVDA et jusqu'à nouveaux changements, chaque année dans la première version de NVDA, les programmeurs devront modifier la version pour correspondre à leur manifeste avec la version NVDA.

Eh bien, il y aura des programmeurs qui le font immédiatement, d'autres qui prennent son temps pour le faire et d'autres qui ne le feront tout simplement pour avoir abandonné leurs extensions ou pour une raison quelconque.

Dans ce dernier cas, nous devrons faire le changement de la propriété lastTestedNVDAVersion à la main et si nous avons de nombreuses extensions, nous devrons perdre du temps, en plus ce n'est pas une tâche facile pour tous les utilisateurs, car il existe de nombreux niveaux d'utilisateurs.

De plus, si nous voulons essayers les versions bêtas et les RC nous devrons modifier ce paramètre dans les manifestes sinon nous ne pouvons pas avoir l'extension installée.

Eh bien, cricricri nous aide dans cette tâche en faisant le processus pour nous et rapidement.

## Utilisation de cricricri

Cricricri peut être lancé à partir du menu Outils / Changeur de date pour les manifestes ou lui ajouter un raccourci allant dans le menu NVDA / Préférences / Gestes de commandes puis rechercher  la catégorie cricricri.

Une fois ouvert, la fenêtre est simple, nous aurons une liste avec nos extensions et sa version dans le manifeste.

Nous pouvons choisir celle que nous souhaitons.

Si nous faisons Tabulation nous avons deux boutons, Sélectionner tout ou Désélectionner tout, peu de choses à dire, cela agira sur la liste des extensions.

Si nous faisons Tabulation nous tomberons dans trois zones de liste déroulantes:

* Sélectionner la version Majeure: Cette zone de liste déroulante  doit correspondre à la date de la version que aura NVDA.

* Sélectionner la version Mineure: Ici en la laissant en 1 il suffit, cependant j'ai mis les quatre versions qui sortent annuellement s'il y avait des changements. (N'importe quoi peut arriver)

* Sélectionner une révision: Dans cette zone de liste déroulante en la laissant en 0 il suffit, cependant j'ai mis  jusqu'à 5 aussi au cas où.

Si nous faisons Tabulation nous tomberons sur le bouton Appliquer les changements aux manifestes, , ce qui commencera le processus  de modification des manifestes pour les extensions que nous avons sélectionnées dans la liste.

Si nous faisons Tabulation une fois de plus nous tombons sur le bouton Fermer, qui fermera la fenêtre sans faire aucune action.

## Raccourcis clavier

* Alt+L: Nous amènera rapidement à la liste des extensions.
* Alt+S: Nous sélectionnons toutes les extensions.
* Alt+D: Nous désélectionnons toutes les extensions qui sont cochées.
* Alt+A: Commencera la modification des manifestes de ces extensions que nous avons sélectionnées.
* Alt+F ou Échap: Fermera  la fenêtre sans effectuer aucune action.

## Observations de l'auteur

Eh bien, NVDA est un lecteur d'écran en évolution constante, il existe donc plusieurs fois de nombreuses extensions qui sont laissées en cours de route en raison du manque de développement et du fait de ne pas les adapter aux changements de NVDA dans son évolution.

Cela signifie que le changement de la date dans les manifestes résout un problème momentané pour continuer à utiliser ces extensions qui ne sont pas mises à jour ou que le développeur prend du temps pour les mettre à jour. Mais il y aura des extensions qui ne serviront pas seulement à changer le manifeste et nécessitent des changements internes  pour s'adapter aux nouvelles versions, dans ce cas, l'extension sera brisée et reste à contacter avec l'auteur de ladite extension.

Bien je conseille de mettre à jour les extensions présentant les changements dans les manifestes, bien que nous ayons changé avec cricricri la date étant possible que ces extensions apportent hormis l'adaptation du manifeste des autres modifications que le développeur a fait.

Dire également que je ne me responsabilise pas si quelque chose se brise pour changer les manifestes car il y a des centaines d'extensions et qu'il peut y avoir une exception non envisagée de ma part.

L'utilisation de cette extension et ses résultats sont exclusivement sous la responsabilité de l'utilisateur final.


## Traducteurs et contributeurs:

* Français: Rémy Ruiz
* Anglais: Alberto Buffolino
* Turc: : umut korkmaz

# Journal des changements.
## Version 0.2.1.

* Résolu une erreur de sécurité sur les écrans sécurisés.

* Résolu un problème avec la recharge des extensions dans NVDA.
 
 * Ajout de la langue en Anglais.