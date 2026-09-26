# Updating the profile

Edit README.md directly in GitHub or locally. No generator, action, or build step is needed. HTML comments are editing guides; they do not appear on the profile.

## Switch the main project

Everything specific to the main project is between FEATURED:START and FEATURED:END: status, title, description, links, screenshot, results, stack, and expandable details. Replace that content together. The header and section graphics are independent of the project and need no edits.

The screenshot, results table, stack paragraph, and details block are optional. Delete an entire optional element when it is not relevant. A project without a screenshot or measurements still works with just its title, description, and link inside the first table.

To keep the former featured project, add its title, repository link, and short description as a Markdown bullet inside ARCHIVE:START. Remove any old archive entry for the new featured project if it would be redundant.

## Change the selected cards

Between SELECTED:START and SELECTED:END, each td element is a self-contained card: decorative image, linked title, description, and stack. Edit those fields or copy a whole td block. Two cards sit inside each tr row.

For an odd number of cards, put the final card alone in a tr and change its td attributes to colspan="2" valign="top" (remove width="50%"). This gives it a full-width row instead of an empty placeholder. Remove an entire tr when deleting both its cards.

The four small illustrations are reusable motifs: assets/identity.svg, assets/network.svg, assets/hybrid.svg, and assets/containers.svg. They contain no project names or links. Choose any motif for a new card, or remove the img element entirely. Keep decorative image alt text empty; the card title supplies its accessible name.

## Change the archive

Between ARCHIVE:START and ARCHIVE:END, add, remove, or reorder individual Markdown bullets. To remove the archive entirely, delete everything between those markers, including the details wrapper. No empty slots or visible editing instructions are needed.

If you remove both the selected cards and the archive, remove the Selected work heading, its named anchor, and the Selected work navigation link as well.

## Preview before saving

- Use GitHub's Preview tab; expand Under the hood and More from the workbench.
- Check that the navigation jumps to the right sections and all project links work.
- Check the status, screenshot, metrics, and technology labels belong to the new project.
- Check narrow and wide layouts. Keep card descriptions short so paired cards remain balanced.

The graphics are local SVG files, with no remote badge service or font dependency. The header animation honors reduced-motion preferences. Project changes require editing only README.md.
