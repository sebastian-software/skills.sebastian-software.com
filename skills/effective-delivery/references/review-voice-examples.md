# PR Review Voice Examples

These examples calibrate PR-specific severity, optionality, reviewer class, and
decision language. They are not a second general prose guide. Apply the Metro
English route in `effective-writing` for natural phrasing, and do not copy these
examples as templates.

**Asking for the missing ticket (step-1 gate, ticket-linking repo):**
"Looks reasonable, but without a linked task I can't really tell what this is
meant to solve — mind linking it?"

**Asking for a second look (the grey-zone approve):**
Input intent: PR is fine but big/tricky, want another human on it.
Output: "Looks good to me, approving so this isn't blocked. Given how much
surface this touches, might be worth having someone from the X side skim it too
before merge."
(Note: framed on scope, not on doubt. No "I'm unsure".)

**Approve, clean work (human author):**
"Nice — this reads really well, especially how you split out the validation.
Approving."

**Approve with a taste-level suggestion (human author):**
"This is in good shape. The narrow migration and the role-transition test are
especially nice. Approving. One small, optional thing: the helper name could be
a little more explicit, but I wouldn't hold the PR for it."

**Request changes (human author):**
"The overall direction is good, and keeping the authorization check close to the
query makes this easy to follow. One thing is blocking for me: this fallback
uses the requested account ID before ownership is verified, so another tenant's
invoice is reachable. Please enforce the tenant check before the lookup and add
a regression test for the cross-tenant case."

**Reply to a bot finding you're fixing:**
"Good catch, fixed — guarding the null case now."

**Reply to a bot finding you're declining:**
"Intentional here: this path only runs after the auth check, so the input is
already validated. Leaving as is."
