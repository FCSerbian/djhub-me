---
title: "{{ brand }} {{ model_name }} Software & Gear Specs Breakdown"
date: 2026-09-16
draft: false
slug: "{{ hardware_id }}"
description: "Is the {{ brand }} {{ model_name }} compatible with your DJ software? Full hardware specs, stem controls, and outputs."
---

# {{ brand }} {{ model_name }} Compatibility & Tech Specs

The **{{ brand }} {{ model_name }}** is a {{ channels }}-channel {{ device_type.lower() }} priced at approximately **£{{ price_gbp }}**. 

---

## At a Glance Specs
* **Device Type:** {{ device_type }}
* **Mixer Channels:** {{ channels }}
* **Jog Wheel Size:** {{ jog_wheel_size_mm }}mm
* **Master Outputs:** {{ master_outputs }}
* **Weight:** {{ weight_kg }} kg

---

## Software Support Matrix
* **rekordbox (Mac/Win):** {{ '✅ Native Support' if rekordbox_mac_win else '❌ No Native Support' }}
* **Serato DJ:** {{ '✅ ' + serato_mac_win if serato_mac_win != 'None' else '❌ Not Supported' }}
* **djay Pro:** {{ '✅ Native Support' if djay_pro_mac_win else '❌ Manual Mapping Required' }}
* **iOS / iPadOS:** {{ '✅ Compatible' if ios_support else '❌ Not Supported' }}
* **Android:** {{ '✅ Compatible' if android_support else '❌ Not Supported' }}

---

## Jog Wheel & Hardware Analysis
{{ jog_analysis }}

---

## Stems & Advanced Features
* **Dedicated Stem Controls:** {{ 'Yes' if dedicated_stems else 'No' }}
* **Stem FX Control:** {{ 'Yes' if stems_fx_control else 'No' }}
* **Dual USB (B2B Handovers):** {{ 'Yes' if dual_usb else 'No' }}