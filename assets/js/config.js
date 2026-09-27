/* BetterKid.com — site configuration. Edit values here; no other file needs changes.
   NOTE: the contact address is stored base64-encoded so it never appears in plain text
   anywhere in the source. Decoded at runtime only when a link/form is used. */
window.BK_CONFIG = {
  siteName: "BetterKid.com",
  siteUrl: "https://betterkid.com",
  // Base64 of the single contact address used for every form and every contact link.
  contactB64: "d2Vid29ya3NhMUBnbWFpbC5jb20=",
  // FormSubmit.co is used as the zero-backend form relay (works on GitHub Pages).
  // First submission triggers a one-time activation email to the inbox above.
  formEndpoint: "https://formsubmit.co/",
  // Google AdSense — paste your publisher ID (ca-pub-XXXXXXXXXXXXXXXX) to activate all ad slots.
  adsenseClient: "",
  // YouTube — channel handle + video IDs used by the /videos hub and in-article players.
  youtube: {
    channelHandle: "@BetterKid",
    channelUrl: "https://www.youtube.com/@BetterKid",
    featured: [
      { id: "", title: "Welcome to BetterKid — replace with your video ID", tag: "Start here" },
      { id: "", title: "5 calm-down scripts that actually work (ages 3–8)", tag: "Behavior" },
      { id: "", title: "How much screen time is too much? A simple budget", tag: "Screens" },
      { id: "", title: "Chores & allowance: the 3-jar method", tag: "Money" },
      { id: "", title: "Bedtime routine that ends the battle", tag: "Sleep" },
      { id: "", title: "Raising a reader: 10 minutes a day", tag: "Learning" }
    ]
  },
  // Donation / support rails (all optional — leave blank to hide a button).
  support: {
    paypal: "",         // e.g. https://www.paypal.com/donate/?hosted_button_id=XXXX
    buyMeACoffee: "",   // e.g. https://www.buymeacoffee.com/betterkid
    kofi: "",           // e.g. https://ko-fi.com/betterkid
    patreon: "",        // e.g. https://www.patreon.com/betterkid
    githubSponsors: ""  // e.g. https://github.com/sponsors/webworksa1
  },
  // Affiliate: Amazon Associates tag appended to product links in gift guides.
  amazonTag: "betterkid-20",
  // The mandatory acquisition / sponsorship notice link shown at the top of every page.
  ownerContactUrl: "https://web.works/contact",
  // Social handles (blank = hidden)
  social: { youtube: "https://www.youtube.com/@BetterKid", pinterest: "", instagram: "", facebook: "", x: "" },
  analytics: { ga4: "" } // e.g. G-XXXXXXXXXX
};
