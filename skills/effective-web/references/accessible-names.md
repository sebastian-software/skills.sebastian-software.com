# Accessible Names and Descriptions

Treat the accessible name as the control's primary identifier, not as hidden
copy added after the interface is built. Keep visible language, programmatic
names, descriptions, localization, and speech input aligned.

## Name, label, and description

- The visible label is what sighted users read. The accessible name is what
  assistive technology uses to identify the element. They should normally be
  the same phrase.
- A description adds secondary help or context. It must not carry the action,
  destination, or other information needed to identify the control.
- Inspect the computed accessibility tree when naming is uncertain. Do not
  infer the final name from one attribute in isolation: native text, labels,
  referenced elements, and ARIA participate in an ordered computation.
- Keep names stable while focus remains on a control. Announce a changed state
  through the control's state or nearby status, not by repeatedly rewriting its
  identity.

## Choose the naming technique deliberately

Prefer techniques in this order unless the component has a specific reason to
deviate:

1. Use native content and associations: button text, link text, `label`,
   `legend`, `caption`, `alt`, or an element's established host-language name.
2. Use `aria-labelledby` when visible text elsewhere already supplies the
   label or several visible fragments must be combined.
3. Use `aria-label` only when no suitable visible or referenced label exists.

`aria-label` is convenient but easy to misuse. It can override descendant text,
hide a translation gap, drift from visible copy, and create a name on roles that
should not be named. Verify that the target role permits naming and that the
string goes through the same localization and content-review path as visible
copy.

When using `aria-labelledby`:

- Reference rendered, unique ids in the intended reading order.
- Include the visible label first, then distinguishing context.
- Expect referenced text to become part of the name even when the referenced
  element is visually hidden.
- Recheck the computed name after conditional rendering; a missing id reference
  silently removes context.

## Preserve visible language in the name

- Ensure the accessible name contains the visible label, preferably at the
  beginning. This supports WCAG Label in Name and lets speech-input users say
  what they see.
- Do not replace visible `Search` with `Find products in our complete catalogue`
  through `aria-label`. Keep `Search` in the computed name and place the extra
  explanation in a description when it is useful.
- Distinguish repeated controls without erasing their visible text. For repeated
  `Add to cart` buttons, combine the button text with the product name through
  `aria-labelledby`, or include visually hidden context inside the button.
- Avoid generic visible labels such as `Read more` when the design can use
  meaningful link text. When editorial constraints require repeated short text,
  add the article title as contextual name content and verify the resulting
  link list remains understandable.

## Icon-only controls

Use a native `button` or link, then provide a durable text alternative. Prefer
visually hidden text inside the control because it shares the normal content,
localization, and naming path:

```html
<button type="button">
  <svg aria-hidden="true" focusable="false"><!-- icon --></svg>
  <span class="visually-hidden">Close dialog</span>
</button>
```

Use `aria-label="Close dialog"` when component constraints make real text
impractical, but test the computed name and translation. Do not rely on an SVG
`title`, file name, CSS-generated content, tooltip, or the icon's visual meaning
to name the parent control. Hide a decorative icon from the accessibility tree
so it cannot duplicate or pollute the control name.

For a standalone informative SVG, use an image role and a tested name. For a
decorative SVG, remove it from the accessibility tree. When the SVG is inside a
named control, the SVG is normally decorative even if the same artwork would be
informative on its own.

## Images and alternatives

Choose the alternative from the image's purpose in context, not from what the
pixels contain:

- Use concise `alt` text when the image conveys information not present nearby.
- Use `alt=""` when the image is decorative or repeats adjacent content.
- For a linked image, describe the link's destination or action when no other
  link text supplies the name.
- Do not begin with `image of` unless the medium itself matters.
- Move complex data, instructions, and chart interpretation into nearby HTML;
  `alt` is not a container for a long report.
- Do not use a missing `alt` attribute as shorthand for decorative. A missing
  attribute can expose a file name or other unreliable fallback.

## Descriptions and help text

- Use `aria-describedby` for concise supplementary text such as format help or
  a field error. Keep the label sufficient to identify the control without it.
- Use `aria-description` only when there is no appropriate visible description
  to reference and the target support matrix has been verified.
- Use `aria-details` for a relationship to structured or extended content that
  users may navigate separately; do not assume every screen-reader/browser pair
  exposes it equally well.
- Avoid putting critical instructions only in descriptions. Some users navigate
  by control names or suppress verbose descriptions.
- Do not concatenate every hint, error, counter, and policy sentence into one
  enormous description. Expose the information at the point it becomes useful.

## Verification

For each consequential control, check:

1. The visible label accurately describes the action or destination.
2. The accessibility tree exposes the intended role, name, description, state,
   and relationships.
3. The visible label is contained in the name in the same order.
4. Repeated controls remain distinguishable in a links or controls list.
5. The name remains correct after translation, loading, validation, and state
   changes.
6. The control can be found and activated with representative speech input and
   screen-reader/browser pairings when the flow is consequential.
