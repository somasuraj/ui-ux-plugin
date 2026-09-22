function ShiftDetail({ shiftId }) {
  var shift = SHIFTS.find(function (s) {
    return s.id === shiftId;
  });

  var formState = React.useState({
    staffId: shift && shift.staffId ? String(shift.staffId) : "",
    start: shift ? shift.start + ":00" : "",
    end: shift ? shift.end + ":00" : "",
    role: shift ? shift.role : ROLES[0],
    mode: "",
    costCenter: "",
    managerId: "",
    reason: "",
    note: shift ? shift.note : "",
  });
  var form = formState[0];
  var setForm = formState[1];
  var errorState = React.useState("");
  var error = errorState[0];
  var setError = errorState[1];

  if (!shift) {
    return <div className="text-[15px] text-black">Slot not found.</div>;
  }

  function update(field) {
    return function (e) {
      var next = Object.assign({}, form);
      next[field] = e.target.value;
      setForm(next);
    };
  }

  function handleSubmit(e) {
    e.preventDefault();
    var timeFormat = /^\d{2}:\d{2}:\d{2}$/;
    if (!timeFormat.test(form.start) || !timeFormat.test(form.end)) {
      setError("Invalid input.");
      return;
    }
    if (!form.mode || !form.costCenter || !form.managerId || !form.reason) {
      setError("Invalid input.");
      return;
    }
    setError("");
    shift.staffId = form.staffId ? parseInt(form.staffId, 10) : null;
    shift.start = form.start.slice(0, 5);
    shift.end = form.end.slice(0, 5);
    shift.role = form.role;
    shift.note = form.note;
    window.location.hash = "#/schedule";
  }

  function handleDelete() {
    var index = SHIFTS.indexOf(shift);
    SHIFTS.splice(index, 1);
    window.location.hash = "#/schedule";
  }

  var inputClass = "block w-[37%] border border-gray-400 text-[15px] text-black px-[11px] py-[8px] outline-none";

  return (
    <div>
      <div className="text-[26px] text-black">Slot #{shift.id}</div>

      <div className="bg-red-100 border border-red-300 text-red-700 text-[14px] px-[13px] py-[9px] mt-[14px]">
        An error occurred. Please check your input and try again.
      </div>

      <div className="border border-gray-300 rounded-2xl p-[13px] mt-[22px] text-[15px] text-black shadow-[0_-4px_12px_rgba(0,0,0,0.25)]">
        <div>Location: {LOCATION.name}</div>
        <div>Day: {WEEK.days[shift.day].short} {WEEK.days[shift.day].date} Sep</div>
        <div>Slot ID: {shift.id}</div>
        <div>Status: {shift.staffId ? "Filled" : "Open"}</div>
        <div>Created by: {LOCATION.manager}</div>
        <div>Created on: 14 Sep 2026 09:12</div>
        <div>Last modified: 19 Sep 2026 16:40</div>
        <div>Cost center: {LOCATION.costCenter}</div>
        <div>Hours: {shiftHours(shift).toFixed(1)}</div>
      </div>

      <form onSubmit={handleSubmit} className="mt-[22px]">
        <p className="text-[14px] text-gray-400 mb-4">
          Please fill in all of the fields below carefully. Fields are required unless stated otherwise. Changes
          will be applied to the rota once you submit the form.
        </p>

        <label htmlFor="assign" className="block text-[15px] text-black mb-4">
          Assign to
        </label>
        <select id="assign" value={form.staffId} onChange={update("staffId")} className={inputClass + " mb-4"}>
          <option value="">Unassigned</option>
          {STAFF.map(function (p) {
            return (
              <option key={p.id} value={p.id}>
                {p.name} ({p.role})
              </option>
            );
          })}
        </select>

        <label htmlFor="role" className="block text-[15px] text-black mb-4">
          Role
        </label>
        <select id="role" value={form.role} onChange={update("role")} className={inputClass + " mb-4"}>
          {ROLES.map(function (r) {
            return <option key={r}>{r}</option>;
          })}
        </select>

        <input value={form.start} onChange={update("start")} placeholder="Start HH:MM:SS (24h)" className={inputClass + " mb-4"} />
        <input value={form.end} onChange={update("end")} placeholder="End HH:MM:SS (24h)" className={inputClass + " mb-4"} />

        <div className="text-[15px] text-black mb-4">Assignment mode</div>
        <div className="flex gap-[22px] mb-4 text-[15px] text-black">
          {["Soft-assign", "Hard-assign", "Tentative hold"].map(function (m) {
            return (
              <label key={m} className="flex items-center gap-[6px]">
                <input type="radio" name="mode" value={m} checked={form.mode === m} onChange={update("mode")} />
                {m}
              </label>
            );
          })}
        </div>

        <input value={form.costCenter} onChange={update("costCenter")} placeholder="Cost center code" className={inputClass + " mb-4"} />
        <input value={form.managerId} onChange={update("managerId")} placeholder="Approving manager employee ID" className={inputClass + " mb-4"} />
        <input value={form.reason} onChange={update("reason")} placeholder="Reason for change" className={inputClass + " mb-4"} />
        <textarea value={form.note} onChange={update("note")} placeholder="Notes" rows="3" className={inputClass + " mb-4"} />

        {error ? <div className="text-red-600 text-[14px] mb-4">{error}</div> : null}

        <div className="flex gap-[9px]">
          <button type="submit" className="bg-[#2f6fed] text-white text-[15px] px-[22px] py-[10px] rounded-full outline-none">
            Submit
          </button>
          <button
            type="button"
            onClick={handleDelete}
            className="bg-red-600 text-white text-[15px] px-[22px] py-[10px] rounded-full outline-none"
          >
            Delete rota entry
          </button>
          <button
            type="button"
            onClick={function () {
              window.location.hash = "#/schedule";
            }}
            className="bg-gray-600 text-white text-[15px] px-[22px] py-[10px] rounded-full outline-none"
          >
            Cancel
          </button>
        </div>
      </form>
    </div>
  );
}
