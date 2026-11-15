# Urban nature

Target assets: deciduous and conifer trees, street trees in tree pits, hedges, shrubs, grass, flower beds, park vegetation and riverbank planting.

For performance, prefer LODs, billboards or impostors for distant vegetation and instancing for repeated species. Record season, leaf state, approximate height and texture requirements.

## Bark and leaf textures (MIT)

`textures/bark_{oak,birch,pine}_{c,n}.jpg` (colour, normal) and `textures/leaf_{oak,ash,pine}.png` (twig cards with alpha), resized to 512 px. Source: ez-tree by Daniel Greenheck, https://github.com/dgreenheck/ez-tree, MIT License (see `textures/LICENSE-ez-tree.txt`). Used in Sunset Coast for procedurally generated branching trees: bark tubes plus crossed twig cards, alpha test about 0.42, alpha-tested shadow depth material.
