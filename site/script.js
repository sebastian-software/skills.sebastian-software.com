const root = document.documentElement
const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)")

const copyText = async (text) => {
  if (navigator.clipboard && window.isSecureContext) {
    try {
      await Promise.race([
        navigator.clipboard.writeText(text),
        new Promise((_, reject) => {
          window.setTimeout(() => reject(new Error("Clipboard timed out")), 600)
        }),
      ])
      return
    } catch {
      // Continue with the selection-based fallback below.
    }
  }

  const textArea = document.createElement("textarea")
  textArea.value = text
  textArea.setAttribute("readonly", "")
  textArea.style.position = "fixed"
  textArea.style.opacity = "0"
  document.body.append(textArea)
  textArea.select()
  const copied = document.execCommand("copy")
  textArea.remove()

  if (!copied) {
    throw new Error("Copy command was rejected")
  }
}

const copyStatus = document.querySelector("[data-copy-status]")

for (const button of document.querySelectorAll("[data-copy-target]")) {
  const target = document.getElementById(button.dataset.copyTarget)
  const label = button.querySelector("[data-copy-label]")

  if (!target || !label) continue

  const originalLabel = label.textContent
  let resetTimer

  button.addEventListener("click", async () => {
    window.clearTimeout(resetTimer)

    try {
      await copyText(target.textContent.trim())
      label.textContent = "Copied"
      if (copyStatus) copyStatus.textContent = "Command copied to clipboard."
    } catch {
      label.textContent = "Select"
      window.getSelection()?.selectAllChildren(target)
      if (copyStatus) copyStatus.textContent = "Copy was unavailable. Command selected."
    }

    resetTimer = window.setTimeout(() => {
      label.textContent = originalLabel
    }, 1800)
  })
}

const filterButtons = [...document.querySelectorAll("[data-filter]")]
const skillCards = [...document.querySelectorAll("[data-skill]")]
const filterStatus = document.querySelector("[data-filter-status]")

for (const button of filterButtons) {
  button.addEventListener("click", () => {
    const filter = button.dataset.filter
    let visibleCount = 0

    for (const candidate of filterButtons) {
      candidate.setAttribute("aria-pressed", String(candidate === button))
    }

    for (const card of skillCards) {
      const visible = filter === "all" || card.dataset.category === filter
      card.hidden = !visible
      if (visible) visibleCount += 1
    }

    if (filterStatus) {
      const category = button.firstChild?.textContent?.trim() || "selected"
      filterStatus.textContent =
        filter === "all"
          ? `${visibleCount} skills shown.`
          : `${visibleCount} ${category.toLowerCase()} skills shown.`
    }
  })
}

const revealElements = [...document.querySelectorAll(".reveal")]

if (!reduceMotion.matches && "IntersectionObserver" in window) {
  root.classList.add("reveal-ready")

  const revealObserver = new IntersectionObserver(
    (entries, observer) => {
      for (const entry of entries) {
        if (!entry.isIntersecting) continue
        entry.target.classList.add("is-visible")
        observer.unobserve(entry.target)
      }
    },
    { rootMargin: "0px 0px -8%", threshold: 0.08 },
  )

  for (const element of revealElements) revealObserver.observe(element)
}

const systemVisual = document.querySelector("[data-system-visual]")
const finePointer = window.matchMedia("(hover: hover) and (pointer: fine)")

if (systemVisual && finePointer.matches && !reduceMotion.matches) {
  let pointerFrame = 0

  systemVisual.addEventListener("pointermove", (event) => {
    if (pointerFrame) cancelAnimationFrame(pointerFrame)

    pointerFrame = requestAnimationFrame(() => {
      const bounds = systemVisual.getBoundingClientRect()
      const x = (event.clientX - bounds.left) / bounds.width - 0.5
      const y = (event.clientY - bounds.top) / bounds.height - 0.5
      systemVisual.style.setProperty("--tilt-x", `${y * -4}deg`)
      systemVisual.style.setProperty("--tilt-y", `${x * 4}deg`)
    })
  })

  systemVisual.addEventListener("pointerleave", () => {
    systemVisual.style.setProperty("--tilt-x", "0deg")
    systemVisual.style.setProperty("--tilt-y", "0deg")
  })
}

const header = document.querySelector("[data-header]")

const updateHeader = () => {
  header?.classList.toggle("is-scrolled", window.scrollY > 12)
}

updateHeader()
window.addEventListener("scroll", updateHeader, { passive: true })

const year = document.querySelector("[data-year]")
if (year) year.textContent = String(new Date().getFullYear())
