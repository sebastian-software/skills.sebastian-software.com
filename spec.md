# Arbeitsauftrag: Gemeinsame Verwaltung von Agent Skills

## Ziel

Es soll ein zentraler, reproduzierbarer Workflow entstehen, um Agent Skills zwischen mehreren Rechnern und Kollegen synchron zu halten.

Dabei sollen zwei Arten von Skills unterstützt werden:

1. **Eigene Team-Skills**, die intern entwickelt und gepflegt werden.
2. **Externe Skills**, die von anderen veröffentlicht wurden und z. B. über Git oder `skills-cli` installierbar sind.

Die Lösung soll verhindern, dass einzelne Entwickler unterschiedliche Skill-Versionen nutzen. Externe Skills sollen nicht ungeprüft aktualisiert werden, sondern wie Dependencies behandelt werden: versioniert, reviewbar und nachvollziehbar.

## Grundsatzentscheidung

Die Skills werden über ein zentrales Git-Repository verwaltet.

Dieses Repository ist die verbindliche Quelle für alle freigegebenen Skills. Lokale Installationen werden daraus generiert oder per Symlink angebunden.

Externe Skills werden nicht direkt auf den Entwicklerrechnern produktiv aktualisiert, sondern zunächst in das zentrale Repository übernommen. Änderungen an externen Skills laufen über Pull Requests und können dadurch geprüft werden.

## Vorgeschlagene Repository-Struktur

```txt
agent-skills/
  README.md

  skills/
    own/
      react-architecture-review/
        SKILL.md
        references/
        scripts/

      i18n-lingui-review/
        SKILL.md
        references/
        scripts/

    vendor/
      openai-spreadsheets/
        SKILL.md
        references/
        scripts/
        SOURCE.md

      community-skill-x/
        SKILL.md
        SOURCE.md

  manifests/
    skills.sources.json
    skills.lock.json

  scripts/
    install.sh
    update-vendor.sh
    validate-skills.sh
```

## Bedeutung der Verzeichnisse

### `skills/own`

Hier liegen alle intern gepflegten Skills.

Diese Skills werden direkt im Repository bearbeitet. Änderungen erfolgen über normale Pull Requests.

Beispiele:

* Architektur-Review für React-Projekte
* i18n-/Lingui-Migration
* Sanity-Image-Pipeline
* Projekt-Setup-Review
* Codebase-Audit

### `skills/vendor`

Hier liegen geprüfte externe Skills.

Diese Skills stammen aus öffentlichen Repositories oder anderen Quellen, werden aber bewusst in dieses Repository übernommen. Dadurch kann das Team exakt nachvollziehen, welche Version genutzt wird.

Jeder externe Skill erhält zusätzlich eine `SOURCE.md`.

Beispiel:

```md
# Source

Original source: https://github.com/example/agent-skills
Imported at: 2026-06-09
Imported ref: abc123
Reviewed by: Sebastian Werner
Local modifications: no
License: MIT
```

### `manifests/skills.sources.json`

Diese Datei beschreibt, welche externen Skills grundsätzlich beobachtet oder importiert werden sollen.

Beispiel:

```json
{
  "vendor": [
    {
      "id": "openai-skills",
      "repo": "https://github.com/openai/skills",
      "ref": "main",
      "include": ["spreadsheets", "pdfs", "docs"]
    },
    {
      "id": "community-skill-x",
      "repo": "https://github.com/example/community-skills",
      "ref": "v1.2.0",
      "include": ["skill-x"]
    }
  ]
}
```

### `manifests/skills.lock.json`

Diese Datei hält fest, welche konkrete Version eines externen Skills aktuell im Team verwendet wird.

Beispiel:

```json
{
  "openai-skills": {
    "commit": "abc123",
    "updatedAt": "2026-06-09",
    "included": ["spreadsheets", "pdfs", "docs"]
  },
  "community-skill-x": {
    "commit": "def456",
    "updatedAt": "2026-06-09",
    "included": ["skill-x"]
  }
}
```

## Installation auf Entwicklerrechnern

Die lokale Installation soll über ein Script erfolgen.

Beispiel:

```bash
./scripts/install.sh
```

Das Script soll:

1. den lokalen Agent-Skill-Ordner vorbereiten,
2. die freigegebenen Skills aus `skills/own` und `skills/vendor` verfügbar machen,
3. optional Symlinks setzen,
4. bestehende Installationen kontrolliert ersetzen oder aktualisieren.

Beispiel für eine einfache Symlink-Variante:

```bash
#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
TARGET_DIR="$HOME/.agents/skills"

mkdir -p "$HOME/.agents"

rm -rf "$TARGET_DIR"
ln -s "$REPO_DIR/skills" "$TARGET_DIR"

echo "Agent Skills installed from: $REPO_DIR/skills"
```

Hinweis: Falls die Zielumgebung keine verschachtelte Struktur wie `skills/own/...` und `skills/vendor/...` unterstützt, soll das Script stattdessen einen flachen `dist/skills`-Ordner generieren.

## Generierter Installationsordner

Optional kann ein `dist/`-Ordner erzeugt werden:

```txt
agent-skills/
  dist/
    skills/
      react-architecture-review/
      i18n-lingui-review/
      openai-spreadsheets/
      community-skill-x/
```

In diesem Fall installiert `install.sh` nicht direkt `skills/`, sondern `dist/skills`.

Das ist robuster, wenn Quellstruktur und Zielstruktur unterschiedlich sein sollen.

## Aktualisierung externer Skills

Externe Skills sollen über ein dediziertes Script aktualisiert werden.

Beispiel:

```bash
./scripts/update-vendor.sh
```

Das Script soll:

1. `manifests/skills.sources.json` lesen,
2. externe Repositories temporär klonen oder per `skills-cli` aktualisieren,
3. die gewünschten Skills nach `skills/vendor` kopieren,
4. `SOURCE.md` aktualisieren,
5. `manifests/skills.lock.json` aktualisieren,
6. Änderungen im Git-Diff sichtbar machen.

Der Update-Prozess endet bewusst nicht mit automatischer Veröffentlichung. Stattdessen wird ein Pull Request erstellt.

Beispiel-Workflow:

```bash
./scripts/update-vendor.sh

git diff

git checkout -b update-vendor-skills-2026-06-09
git add .
git commit -m "Update vendor skills"
git push
```

Danach erfolgt ein Review.

## Review-Regeln für externe Skills

Vor der Übernahme oder Aktualisierung eines externen Skills sollen folgende Punkte geprüft werden:

1. Ist die Quelle vertrauenswürdig?
2. Ist die Lizenz kompatibel?
3. Enthält der Skill unerwünschte oder riskante Instruktionen?
4. Enthält der Skill Skripte oder ausführbaren Code?
5. Greift der Skill auf sensible Dateien, Umgebungsvariablen oder externe Dienste zu?
6. Überschreibt der Skill Verhalten, das für unsere Projekte problematisch wäre?
7. Ist der Skill für unsere konkrete Nutzung wirklich relevant?

Externe Skills werden erst nach Review in `skills/vendor` übernommen.

## Umgang mit Submodules

Git Submodules werden nicht als Standard verwendet.

Submodules können eingesetzt werden, wenn ein externes Skill-Repository exakt referenziert werden soll und keine lokalen Änderungen geplant sind.

Für den normalen Team-Workflow wird jedoch ein vendorter Stand bevorzugt, weil dieser einfacher zu klonen, zu reviewen und zu installieren ist.

Empfohlene Regel:

* **Submodule** nur für große, stabile externe Skill-Sammlungen.
* **Vendoring** für einzelne oder angepasste Skills.
* **Manifest + Lockfile** für nachvollziehbare Updates.

## Validierung

Es soll ein einfaches Validierungsscript geben:

```bash
./scripts/validate-skills.sh
```

Dieses Script soll prüfen:

1. Jeder Skill enthält eine `SKILL.md`.
2. Jede `SKILL.md` enthält mindestens `name` und `description`.
3. Skill-Namen sind eindeutig.
4. Externe Skills enthalten eine `SOURCE.md`.
5. Es gibt keine doppelten Zielnamen im generierten Installationsordner.
6. Optional: bekannte riskante Pattern werden markiert.

Beispiele für zu prüfende riskante Pattern:

```txt
rm -rf
curl ... | sh
eval
printenv
cat ~/.ssh
cat ~/.env
```

Die Prüfung muss nicht perfekt sein. Sie soll vor allem grobe Fehler und offensichtliche Risiken sichtbar machen.

## Vorgeschlagener Entwickler-Workflow

### Erstinstallation

```bash
git clone git@github.com:company/agent-skills.git ~/dev/agent-skills
cd ~/dev/agent-skills
./scripts/install.sh
```

### Skills aktualisieren

```bash
cd ~/dev/agent-skills
git pull
./scripts/install.sh
```

### Eigenen Skill hinzufügen

```bash
mkdir -p skills/own/my-new-skill
touch skills/own/my-new-skill/SKILL.md
```

Danach:

```bash
./scripts/validate-skills.sh
git checkout -b add-my-new-skill
git add .
git commit -m "Add my new skill"
git push
```

### Externen Skill aktualisieren

```bash
./scripts/update-vendor.sh
./scripts/validate-skills.sh
git diff
```

Danach Pull Request erstellen.

## Akzeptanzkriterien

Die Umsetzung gilt als abgeschlossen, wenn:

1. Ein zentrales `agent-skills` Repository existiert.
2. Eigene Skills unter `skills/own` abgelegt werden können.
3. Externe Skills unter `skills/vendor` abgelegt werden können.
4. Jeder externe Skill eine `SOURCE.md` enthält.
5. Ein `install.sh` die Skills lokal verfügbar macht.
6. Ein `update-vendor.sh` externe Skills kontrolliert aktualisieren kann.
7. Ein `validate-skills.sh` die wichtigsten Strukturregeln prüft.
8. Ein `skills.lock.json` die aktuell verwendeten externen Skill-Versionen dokumentiert.
9. Der Workflow in der `README.md` beschrieben ist.
10. Änderungen an Skills über Pull Requests reviewbar sind.

## Nicht-Ziele

Folgende Punkte sind zunächst ausdrücklich nicht Teil der Umsetzung:

1. Automatische Live-Aktualisierung auf Entwicklerrechnern.
2. Ungeprüfte Installation externer Skills.
3. Vollständiger Package-Manager für Skills.
4. Komplexe Rechteverwaltung pro Skill.
5. Automatische Veröffentlichung in ChatGPT Workspaces.
6. Vollständige Security-Analyse externer Skripte.

## Ergebnis

Am Ende gibt es einen einfachen, robusten und teamfähigen Workflow:

* Git ist die zentrale Quelle.
* Eigene Skills werden direkt gepflegt.
* Externe Skills werden kontrolliert übernommen.
* Versionen sind nachvollziehbar.
* Updates sind reviewbar.
* Entwickler installieren oder aktualisieren Skills mit einem einfachen Script.

Damit bleibt die Nutzung von Agent Skills flexibel, aber trotzdem reproduzierbar und sicher genug für den professionellen Team-Einsatz.
