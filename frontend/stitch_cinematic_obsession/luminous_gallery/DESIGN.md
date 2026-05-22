---
name: Luminous Gallery
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f3'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#3d4947'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#6c7a77'
  outline-variant: '#bcc9c6'
  surface-tint: '#006a62'
  primary: '#006a62'
  on-primary: '#ffffff'
  primary-container: '#00a396'
  on-primary-container: '#00302c'
  inverse-primary: '#5ddacb'
  secondary: '#5e5e63'
  on-secondary: '#ffffff'
  secondary-container: '#e0dfe5'
  on-secondary-container: '#626267'
  tertiary: '#006a64'
  on-tertiary: '#ffffff'
  tertiary-container: '#00a39b'
  on-tertiary-container: '#00312e'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#7cf6e7'
  primary-fixed-dim: '#5ddacb'
  on-primary-fixed: '#00201d'
  on-primary-fixed-variant: '#005049'
  secondary-fixed: '#e3e2e7'
  secondary-fixed-dim: '#c7c6cb'
  on-secondary-fixed: '#1a1b20'
  on-secondary-fixed-variant: '#46464b'
  tertiary-fixed: '#62f9ee'
  tertiary-fixed-dim: '#3cdcd1'
  on-tertiary-fixed: '#00201e'
  on-tertiary-fixed-variant: '#00504b'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Inter
    fontSize: 28px
    fontWeight: '600'
    lineHeight: 36px
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin-desktop: 64px
  margin-mobile: 20px
---

## Brand & Style

The design system transitions from a "dark theater" aesthetic to a "bright gallery" experience. It is defined by an airy, high-end, and modern personality that prioritizes clarity, breathability, and premium finishes. The target audience values sophisticated presentation and effortless navigation within a content-rich environment.

The visual style is a blend of **Minimalism** and **Modern Corporate**, utilizing expansive whitespace to create a sense of luxury. By moving away from heavy shadows and dark backgrounds, the system evokes an emotional response of openness and professional transparency. The "immersive" quality is maintained through deliberate use of scale and high-quality imagery rather than visual density.

## Colors

The palette is anchored by a soft white background (`#FAFAFA`) that provides a clean canvas for content. Surfaces such as cards and modals use pure white (`#FFFFFF`) to create subtle, tiered separation without the need for heavy borders. 

The primary accent is a refined, deeper version of cyan (`#00A396`) to ensure AA accessibility for text and interactive elements against light backgrounds, while the original vibrant cyan (`#66FCF1`) is reserved for decorative highlights or low-stakes UI elements like progress bars. Typography utilizes a high-contrast deep charcoal (`#121317`) for headings to maintain authority, paired with a soft grey-black for body text to reduce eye strain.

## Typography

This design system exclusively utilizes **Inter** to maintain a systematic and utilitarian feel that allows content to remain the focus. The hierarchy is intentionally dramatic; large display headings use tighter letter spacing and heavy weights to mimic cinematic posters, while body text remains grounded and highly legible.

For mobile devices, headline sizes scale down to prevent awkward line breaks, ensuring the "Gallery" feel remains consistent across smaller viewports. Labels and small utility text use a slightly increased letter spacing and medium weights to ensure they don't get lost against the light UI surfaces.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model for desktop to maintain the "Gallery" curation feel, centering content within a 1280px container. On smaller screens, the system transitions to a fluid model with generous 20px safe margins.

Spacing follows a strict 8px rhythmic scale. To achieve the "Airy" vibe, vertical spacing between major sections should be aggressive (typically 80px to 120px on desktop), allowing each content block to feel like a standalone exhibit. Gutters are kept wide at 24px to ensure the UI never feels cramped.

## Elevation & Depth

Depth is conveyed through **Tonal Layering** and **Ambient Shadows**. Instead of traditional dark shadows, this design system uses highly diffused, low-opacity shadows with a hint of the secondary color (charcoal) to ground elements.

1.  **Level 0 (Background):** `#FAFAFA` – The base canvas.
2.  **Level 1 (Cards/Surfaces):** `#FFFFFF` – Lifted with a 1px soft grey border (#E5E7EB) or a very subtle shadow (Y: 4px, Blur: 20px, 4% Opacity).
3.  **Level 2 (Modals/Popovers):** `#FFFFFF` – Higher elevation with a more pronounced shadow (Y: 12px, Blur: 40px, 8% Opacity) and a backdrop blur on the background layer to maintain the "Immersive" lineage.

## Shapes

The shape language is defined by a consistent 16px radius for primary containers and cards, which corresponds to the `rounded-lg` token in this design system. This moderate roundness strikes a balance between the precision of professional software and the approachability of a lifestyle brand.

Buttons and input fields follow a 8px (0.5rem) radius to feel sturdy and intentional. Interactive chips or tags may utilize pill-shapes to distinguish them from structural elements.

## Components

### Buttons
Primary buttons use the Deep Cyan (`#00A396`) with white text. Secondary buttons are Ghost-style with a 1px border of the primary color or a light grey. All buttons should have a subtle hover state that slightly deepens the background color.

### Input Fields
Inputs are minimal: white background, 1px light grey border, and 16px horizontal padding. On focus, the border transitions to the primary cyan with a soft outer glow.

### Cards
Cards are the primary vehicle for "Immersive" content. They feature the 16px border radius, a white surface, and the Level 1 shadow. Image-heavy cards should use a subtle zoom-in transition on hover to maintain the cinematic feel.

### Chips & Badges
Small, low-contrast grey backgrounds with medium-weight charcoal text. Used for categorization without distracting from the main visual hierarchy.

### Lists
Lists use generous vertical padding (16px - 24px) and subtle 1px dividers. The background of a list item should transition to the background color (`#FAFAFA`) on hover to provide clear feedback.