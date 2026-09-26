# Updating the profile

Edit `README.md` directly, locally or with GitHub's pencil button. No generator, workflow, or extra tools are required. The `<!-- ... -->` comments are editing guides and do not appear on the rendered profile.

## Switch the featured project

1. Find `FEATURED:START` and `FEATURED:END` in `README.md`.
2. Replace the content between those comments: linked title, summary, status, evidence, links, and stack. Keep the section heading and comments.
3. The results table, expandable details, screenshot, and stack line are optional. Delete any that do not suit the new project; the title, summary, and repository link are enough.
4. To keep the previous project visible, add it as one row under `ARCHIVE:START`, using its old title/link and a short description. If the new featured project already has an archive row, remove that row to avoid duplication.

Everything specific to the featured project lives inside that block. The header, navigation, and footer do not need updating when you switch projects. Use an accurate status such as in progress or completed, and remove old screenshots, metrics, and links when replacing the feature.

## Change the other projects

Between `ARCHIVE:START` and `ARCHIVE:END`, each table row is one project. Copy an existing row, change its link and description, and move it wherever you want. Delete a row to remove it. Escape any literal pipe in a title or description as `\|` so it does not create an extra column.

If you remove every project, remove the entire “More projects” section and its navigation link too. Leave no empty table, blank rows, or visible placeholder copy.

## Before saving

- Open GitHub's **Preview** tab and expand **Inside the platform** (or its replacement).
- Check the project links and any image you kept or added.
- Confirm the status and results describe the new project, not the previous one.
- Keep maintenance notes in HTML comments or this guide, outside the public profile copy.
