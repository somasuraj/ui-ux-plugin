var LOCATION = {
  id: "harbour",
  name: "Harbour St",
  address: "14 Harbour Street, Portsmouth, NH 03801",
  phone: "+16035550142",
  timezone: "America/New_York",
  manager: "Maya Rosales",
  costCenter: "CC-4410",
};

var OTHER_LOCATIONS = ["Harbour St", "Mill Lane", "Station Square"];

var WEEK = {
  number: 39,
  label: "21 Sep - 27 Sep",
  days: [
    { key: 0, short: "Mon", date: "21" },
    { key: 1, short: "Tue", date: "22" },
    { key: 2, short: "Wed", date: "23" },
    { key: 3, short: "Thu", date: "24" },
    { key: 4, short: "Fri", date: "25" },
    { key: 5, short: "Sat", date: "26" },
    { key: 6, short: "Sun", date: "27" },
  ],
  today: 1,
};

var ROLES = ["Shift lead", "Barista", "Kitchen", "Cashier"];

var STAFF = [
  { id: 1, name: "Maya Rosales", role: "Shift lead", rate: 18.5, contracted: 24, email: "maya.rosales@shiftboard.test", phone: "603-555-0101", status: "active", color: "#2f6fed" },
  { id: 2, name: "Tom Whitaker", role: "Barista", rate: 15.0, contracted: 16, email: "tom.whitaker@shiftboard.test", phone: "603-555-0117", status: "active", color: "#0f766e" },
  { id: 3, name: "Priya Nair", role: "Barista", rate: 15.5, contracted: 16, email: "priya.nair@shiftboard.test", phone: "603-555-0123", status: "active", color: "#9333ea" },
  { id: 4, name: "Deshawn Carter", role: "Kitchen", rate: 16.0, contracted: 24, email: "deshawn.carter@shiftboard.test", phone: "603-555-0138", status: "active", color: "#b45309" },
  { id: 5, name: "Elena Petrova", role: "Cashier", rate: 14.5, contracted: 16, email: "elena.petrova@shiftboard.test", phone: "603-555-0144", status: "active", color: "#be123c" },
  { id: 6, name: "Liam O'Connor", role: "Barista", rate: 15.0, contracted: 16, email: "liam.oconnor@shiftboard.test", phone: "603-555-0159", status: "new", color: "#4d7c0f" },
  { id: 7, name: "Hana Sato", role: "Barista", rate: 15.5, contracted: 16, email: "hana.sato@shiftboard.test", phone: "603-555-0162", status: "active", color: "#0369a1" },
  { id: 8, name: "Marcus Bell", role: "Shift lead", rate: 18.0, contracted: 24, email: "marcus.bell@shiftboard.test", phone: "603-555-0170", status: "active", color: "#7c2d12" },
  { id: 9, name: "Sofia Almeida", role: "Kitchen", rate: 16.5, contracted: 16, email: "sofia.almeida@shiftboard.test", phone: "603-555-0186", status: "active", color: "#a21caf" },
  { id: 10, name: "Jack Thornton", role: "Cashier", rate: 14.5, contracted: 8, email: "jack.thornton@shiftboard.test", phone: "603-555-0191", status: "active", color: "#475569" },
  { id: 11, name: "Amira Haddad", role: "Barista", rate: 15.0, contracted: 8, email: "amira.haddad@shiftboard.test", phone: "603-555-0205", status: "new", color: "#0e7490" },
  { id: 12, name: "Noah Lindqvist", role: "Barista", rate: 15.0, contracted: 16, email: "noah.lindqvist@shiftboard.test", phone: "603-555-0213", status: "leave", color: "#64748b" },
];

var SHIFTS = [
  { id: 1, day: 0, start: "06:30", end: "13:00", role: "Shift lead", staffId: 1, note: "Open up, float count" },
  { id: 2, day: 0, start: "07:00", end: "14:00", role: "Barista", staffId: 2, note: "" },
  { id: 3, day: 0, start: "12:00", end: "18:30", role: "Cashier", staffId: 5, note: "" },
  { id: 4, day: 0, start: "13:00", end: "19:00", role: "Barista", staffId: 3, note: "Close down bar" },
  { id: 5, day: 1, start: "06:30", end: "13:00", role: "Shift lead", staffId: 1, note: "" },
  { id: 6, day: 1, start: "07:00", end: "13:00", role: "Barista", staffId: 7, note: "" },
  { id: 7, day: 1, start: "11:00", end: "17:00", role: "Kitchen", staffId: 4, note: "Bakery delivery at 11:30" },
  { id: 8, day: 1, start: "13:00", end: "19:00", role: "Barista", staffId: null, note: "Noah on leave, needs cover" },
  { id: 9, day: 2, start: "06:30", end: "13:00", role: "Shift lead", staffId: 8, note: "" },
  { id: 10, day: 2, start: "07:00", end: "14:00", role: "Barista", staffId: 2, note: "" },
  { id: 11, day: 2, start: "11:00", end: "17:00", role: "Kitchen", staffId: 9, note: "" },
  { id: 12, day: 2, start: "13:00", end: "19:00", role: "Cashier", staffId: 10, note: "Till training with Elena first hour" },
  { id: 13, day: 3, start: "06:30", end: "13:00", role: "Shift lead", staffId: 1, note: "" },
  { id: 14, day: 3, start: "07:00", end: "13:00", role: "Barista", staffId: 11, note: "Second week, pair with Maya" },
  { id: 15, day: 3, start: "12:00", end: "18:30", role: "Cashier", staffId: null, note: "" },
  { id: 16, day: 4, start: "06:30", end: "13:00", role: "Shift lead", staffId: 1, note: "" },
  { id: 17, day: 4, start: "07:00", end: "14:00", role: "Barista", staffId: 2, note: "" },
  { id: 18, day: 4, start: "11:00", end: "17:00", role: "Kitchen", staffId: 4, note: "" },
  { id: 19, day: 4, start: "13:00", end: "19:00", role: "Barista", staffId: 3, note: "" },
  { id: 20, day: 5, start: "07:00", end: "13:00", role: "Shift lead", staffId: 8, note: "Farmers market day, expect queue" },
  { id: 21, day: 5, start: "08:00", end: "15:00", role: "Barista", staffId: 7, note: "" },
  { id: 22, day: 5, start: "08:00", end: "15:00", role: "Barista", staffId: null, note: "Second bar for market rush" },
  { id: 23, day: 5, start: "11:00", end: "17:00", role: "Kitchen", staffId: 9, note: "" },
  { id: 24, day: 6, start: "08:00", end: "14:30", role: "Shift lead", staffId: 1, note: "" },
  { id: 25, day: 6, start: "09:00", end: "15:00", role: "Cashier", staffId: null, note: "" },
];

function toMinutes(hhmm) {
  var parts = hhmm.split(":");
  return parseInt(parts[0], 10) * 60 + parseInt(parts[1], 10);
}

function shiftHours(shift) {
  return (toMinutes(shift.end) - toMinutes(shift.start)) / 60;
}

function staffById(id) {
  return STAFF.find(function (p) {
    return p.id === id;
  });
}

function hoursFor(staffId) {
  return SHIFTS.filter(function (s) {
    return s.staffId === staffId;
  }).reduce(function (sum, s) {
    return sum + shiftHours(s);
  }, 0);
}

function shiftCountFor(staffId) {
  return SHIFTS.filter(function (s) {
    return s.staffId === staffId;
  }).length;
}

function overtimeCost() {
  return STAFF.reduce(function (sum, p) {
    var extra = Math.max(0, hoursFor(p.id) - p.contracted);
    return sum + extra * p.rate * 1.5;
  }, 0);
}

function shortName(name) {
  var parts = name.split(" ");
  return parts[0] + " " + parts[1].charAt(0) + ".";
}

function avatarFor(person) {
  var initials = person.name
    .split(" ")
    .map(function (w) {
      return w.charAt(0);
    })
    .join("");
  var svg =
    "<svg xmlns='http://www.w3.org/2000/svg' width='64' height='64'>" +
    "<rect width='64' height='64' fill='" + person.color + "'/>" +
    "<text x='32' y='41' font-size='24' text-anchor='middle' fill='#ffffff' font-family='Arial'>" +
    initials +
    "</text></svg>";
  return "data:image/svg+xml;utf8," + encodeURIComponent(svg);
}

var LOGO_SRC =
  "data:image/svg+xml;utf8," +
  encodeURIComponent(
    "<svg xmlns='http://www.w3.org/2000/svg' width='48' height='48' viewBox='0 0 48 48'>" +
      "<rect width='48' height='48' rx='10' fill='#ffffff'/>" +
      "<path d='M12 18h20v10a8 8 0 0 1-8 8h-4a8 8 0 0 1-8-8z' fill='#2f6fed'/>" +
      "<path d='M32 20h3a4 4 0 0 1 0 8h-3' fill='none' stroke='#2f6fed' stroke-width='3'/>" +
      "</svg>"
  );
