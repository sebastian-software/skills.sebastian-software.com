import { getEslintConfig } from "eslint-config-setup";

const config = await getEslintConfig({ node: true, oxlint: true });

config.unshift({
  ignores: [
    "**/dist/**",
    "coverage/**",
    "node_modules/**",
    "pnpm-lock.yaml",
    "skills/**",
    "**/*.json",
    "**/*.md",
  ],
});

config.push({
  files: ["**/*.ts"],
  rules: {
    "@cspell/spellchecker": "off",
    "@typescript-eslint/no-explicit-any": "off",
    "@typescript-eslint/no-unsafe-type-assertion": "off",
    "@typescript-eslint/promise-function-async": "off",
    "@typescript-eslint/strict-void-return": "off",
    complexity: "off",
    "de-morgan/no-negated-conjunction": "off",
    "max-depth": "off",
    "max-params": "off",
    "max-statements": "off",
    "node/hashbang": "off",
    "perfectionist/sort-exports": "off",
    "perfectionist/sort-imports": "off",
    "perfectionist/sort-intersection-types": "off",
    "perfectionist/sort-named-imports": "off",
    "perfectionist/sort-union-types": "off",
    "regexp/no-super-linear-backtracking": "off",
    "regexp/no-useless-quantifier": "off",
    "regexp/prefer-w": "off",
    "regexp/prefer-character-class": "off",
    "regexp/use-ignore-case": "off",
    "security/detect-non-literal-fs-filename": "off",
    "security/detect-unsafe-regex": "off",
    "sonarjs/cognitive-complexity": "off",
    "vitest/prefer-strict-equal": "off",
  },
});

export default config;
