function Settings() {
  var locState = React.useState({
    name: LOCATION.name,
    address: LOCATION.address,
    phone: LOCATION.phone,
    timezone: LOCATION.timezone,
  });
  var loc = locState[0];
  var setLoc = locState[1];

  var prefsState = React.useState({ swaps: true, open: true, overtime: false, digest: true, sms: false });
  var prefs = prefsState[0];
  var setPrefs = prefsState[1];

  var phoneErrorState = React.useState(false);
  var phoneError = phoneErrorState[0];
  var setPhoneError = phoneErrorState[1];

  var archiveState = React.useState(false);
  var archiving = archiveState[0];
  var setArchiving = archiveState[1];
  var confirmState = React.useState("");
  var confirmText = confirmState[0];
  var setConfirmText = confirmState[1];

  function updateLoc(field) {
    return function (e) {
      var next = Object.assign({}, loc);
      next[field] = e.target.value;
      setLoc(next);
    };
  }

  function setPref(field) {
    return function (value) {
      var next = Object.assign({}, prefs);
      next[field] = value;
      setPrefs(next);
    };
  }

  function save() {
    setPhoneError(!/^\+1\d{10}$/.test(loc.phone));
  }

  var fieldClass = "block w-full border border-gray-400 text-[15px] text-black px-[11px] py-[8px] mb-[14px] outline-none";

  var PREF_ROWS = [
    { key: "swaps", label: "Swap requests" },
    { key: "open", label: "Open slots not filled 48h before start" },
    { key: "overtime", label: "Someone goes over contracted hours" },
    { key: "digest", label: "Monday rota digest" },
    { key: "sms", label: "Send by SMS as well as email" },
  ];

  return (
    <div>
      <div className="text-[26px] text-black">Preferences</div>

      <div className="border border-gray-300 p-[13px] mt-[22px]">
        <div className="text-[15px] uppercase text-black mb-[14px]">Location</div>
        <input value={loc.name} onChange={updateLoc("name")} placeholder="Location name" className={fieldClass} />
        <input value={loc.address} onChange={updateLoc("address")} placeholder="Street address" className={fieldClass} />
        <input value={loc.phone} onChange={updateLoc("phone")} placeholder="Phone, format +1XXXXXXXXXX, no spaces or dashes" className={fieldClass} />
        {phoneError ? <div className="text-red-600 text-[14px] mb-[14px]">Error: invalid value.</div> : null}
        <select value={loc.timezone} onChange={updateLoc("timezone")} className={fieldClass}>
          <option>America/New_York</option>
          <option>America/Chicago</option>
          <option>America/Denver</option>
          <option>America/Los_Angeles</option>
        </select>
      </div>

      <div className="border border-gray-300 p-[13px] mt-[22px]">
        <div className="text-[15px] uppercase text-black mb-[14px]">Notifications</div>
        <p className="text-center text-[15px] text-[#8a8a8a] mb-[18px]">
          Shiftboard can let you know when things change at your location so that you never miss anything
          important. Notifications are sent to the email address on your account and, if you turn on the SMS
          option, to the mobile number on your account as well. You can change these preferences at any time and
          they will apply to every location that you manage, not only to the one that is currently selected in
          the side menu.
        </p>
        {PREF_ROWS.map(function (row) {
          return (
            <div key={row.key} className="flex items-center border border-gray-200 px-[11px] py-[9px] mb-[7px]">
              <span className="text-[15px] text-black">{row.label}</span>
              <span className="ml-auto">
                <Toggle on={prefs[row.key]} onChange={setPref(row.key)} />
              </span>
            </div>
          );
        })}
      </div>

      <button onClick={save} className="bg-[#2f6fed] text-white text-[15px] px-[26px] py-[9px] mt-[22px] rounded-none outline-none">
        OK
      </button>

      <section aria-labelledby="danger-heading" className="mt-16 max-w-2xl border-t border-gray-200 pt-8">
        <h2 id="danger-heading" className="text-lg font-semibold text-ink-900">
          Danger zone
        </h2>
        <p className="mt-1 text-sm font-normal text-ink-700">
          Archiving hides {LOCATION.name} from schedules and removes its future shifts. Staff records are kept and you can
          restore the location within 30 days.
        </p>
        {!archiving ? (
          <button
            type="button"
            onClick={function () {
              setArchiving(true);
            }}
            className="mt-4 rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-danger-700 hover:bg-red-50 focus:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-danger-600"
          >
            Archive this location...
          </button>
        ) : (
          <div className="mt-4 rounded-card border border-gray-200 bg-surface p-4">
            <label htmlFor="archive-confirm" className="block text-sm font-medium text-ink-900">
              Type "{LOCATION.name}" to confirm
            </label>
            <input
              id="archive-confirm"
              value={confirmText}
              onChange={function (e) {
                setConfirmText(e.target.value);
              }}
              className="mt-2 w-64 rounded-md border border-gray-300 px-3 py-2 text-sm font-normal text-ink-900 focus:outline-none focus:ring-2 focus:ring-brand-500"
            />
            <div className="mt-4 flex gap-3">
              <button
                type="button"
                disabled={confirmText !== LOCATION.name}
                className="rounded-md bg-danger-600 px-4 py-2 text-sm font-medium text-white hover:bg-danger-700 disabled:cursor-not-allowed disabled:opacity-50 focus:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-danger-600"
              >
                Archive {LOCATION.name}
              </button>
              <button
                type="button"
                onClick={function () {
                  setArchiving(false);
                  setConfirmText("");
                }}
                className="rounded-md px-4 py-2 text-sm font-medium text-ink-700 hover:bg-gray-100 focus:outline-none focus-visible:ring-2 focus-visible:ring-brand-500"
              >
                Keep location
              </button>
            </div>
          </div>
        )}
      </section>
    </div>
  );
}
