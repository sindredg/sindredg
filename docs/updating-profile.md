# Updating the profile

Edit README.md directly in GitHub or locally. No action or build step is needed; the only generated file is the in-progress milestone graphic. HTML comments are editing guides; they do not appear on the profile.

## Update the in-progress project

No project is in progress at the moment, so the README has no in-progress block. To add one, put a heading with assets/in-progress.svg, an in-progress anchor, and a navigation link back, and place the project between IN-PROGRESS:START and IN-PROGRESS:END: title, description, milestone graphic, status line, links, and stack.

For a project with milestones, `python3 scripts/progress-track.py N` from the repository root draws the milestone graphic with N milestones complete. The script still holds the labels, region ranges, and output path of k8s-dr, which is finished; adapt them at the top of the script. Update the status line under the graphic and the image alt text to match.

When the project finishes, move it into FEATURED or the archive, then delete the whole in-progress block, its heading and anchor, and the In progress navigation link. To feature a different ongoing project, replace the block; drop the graphic or adapt the labels and region ranges at the top of the script.

## Switch the main project

Everything specific to the main project is between FEATURED:START and FEATURED:END: status, title, description, links, results, stack, and expandable details. Replace that content together. The header and section graphics are independent of the project and need no edits.

The results row, stack paragraph, and details block are optional. Delete an entire optional element when it is not relevant. A project without measurements still works with just its title, description, and link inside the first table.

To keep the former featured project, add its title, repository link, and short description as a Markdown bullet inside ARCHIVE:START. Remove any old archive entry for the new featured project if it would be redundant.

## Change the selected cards

Between SELECTED:START and SELECTED:END, each td element is a self-contained card: decorative image, linked title, description, and stack. Edit those fields or copy a whole td block. Two cards sit inside each tr row.

For an odd number of cards, put the final card alone in a tr and change its td attributes to colspan="2" valign="top" (remove width="50%"). This gives it a full-width row instead of an empty placeholder. Remove an entire tr when deleting both its cards.

The four small illustrations are reusable motifs: assets/identity.svg, assets/network.svg, assets/hybrid.svg, and assets/containers.svg. They contain no project names or links. Choose any motif for a new card, or remove the img element entirely. Keep decorative image alt text empty; the card title supplies its accessible name.

## Change the archive

Between ARCHIVE:START and ARCHIVE:END, add, remove, or reorder individual Markdown bullets. To remove the archive entirely, delete everything between those markers, including the details wrapper. No empty slots or visible editing instructions are needed.

If you remove both the selected cards and the archive, remove the Selected work heading, its named anchor, and the Selected work navigation link as well.

## Preview before saving

- Use GitHub's Preview tab; expand Under the hood and Other projects.
- Check that the navigation jumps to the right sections and all project links work.
- Check the status, metrics, and technology labels belong to the new project.
- Check narrow and wide layouts. Keep card descriptions short so paired cards remain balanced.

Section headings carry a small status mark: a half-filled circle for work in progress and a filled circle for completed work. The graphics are local SVG files, with no remote badge service or font dependency. The header animation honors reduced-motion preferences. Project changes require editing only README.md.

The header shows only the name, with a decorative abstract animation and no technology-specific labels. Over an 18-second cycle, a control plane sends work to three nodes; the lower node fails, its workloads move to the other two, and after it recovers the load rebalances. Reduced-motion preferences show a static, healthy cluster. There are no labels or live-status indicators to update.
