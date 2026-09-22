function Schedule() {
  var viewState = React.useState("Week");
  var view = viewState[0];
  var setView = viewState[1];

  var openShifts = SHIFTS.filter(function (s) {
    return s.staffId === null;
  });
  var totalHours = SHIFTS.reduce(function (sum, s) {
    return sum + shiftHours(s);
  }, 0);
  var wageBill = SHIFTS.reduce(function (sum, s) {
    var p = s.staffId ? staffById(s.staffId) : null;
    return sum + (p ? shiftHours(s) * p.rate : 0);
  }, 0);

  return (
    <div>
      <div className="text-4xl font-normal text-black">Rota Planner</div>
      <div className="text-2xl font-normal text-black mt-[6px]">Week of {WEEK.label}</div>
      <div className="text-xl font-normal text-black mt-[6px]">{LOCATION.name}</div>

      <p className="text-[15px] text-gray-500 mt-[22px]">
        Welcome to the Rota Planner! This is where you can see everything that is happening at your location
        this week. Each column is a day and each card is a slot. To get started, simply click on any card to
        open it, where you will be able to change who is working, adjust the times, or add notes for your
        team. When you are happy with everything, use the buttons below to share the rota with your crew.
      </p>

      <div className="flex items-center mt-[22px] gap-[9px]">
        <button className="bg-[#2f6fed] text-white text-[15px] px-[17px] py-[9px] rounded-full outline-none">
          Add slot
        </button>
        <button className="bg-indigo-600 text-white text-[15px] px-[17px] py-[9px] rounded-none outline-none">
          Copy last week
        </button>
        <button className="bg-green-600 text-white text-[15px] px-[17px] py-[9px] rounded-2xl outline-none">
          Export
        </button>
        <button className="bg-gray-200 text-gray-400 text-[15px] px-[17px] py-[9px] rounded outline-none">
          Publish week
        </button>

        <div className="ml-auto flex border border-gray-200">
          {["Day", "Week", "Fortnight"].map(function (v) {
            return (
              <button
                key={v}
                onClick={function () {
                  setView(v);
                }}
                className={
                  "px-[15px] py-[7px] text-[14px] text-gray-500 outline-none " +
                  (view === v ? "bg-gray-100" : "bg-gray-50")
                }
              >
                {v}
              </button>
            );
          })}
        </div>
      </div>

      <div className="bg-brand-600 rounded-2xl mt-[22px] p-[13px] flex gap-[44px]">
        <div>
          <div className="text-gray-400 text-[12px] uppercase">Scheduled</div>
          <div className="text-gray-300 text-[19px]">{SHIFTS.length} shifts</div>
        </div>
        <div>
          <div className="text-gray-400 text-[12px] uppercase">Hours</div>
          <div className="text-gray-300 text-[19px]">{totalHours.toFixed(1)}</div>
        </div>
        <div>
          <div className="text-gray-400 text-[12px] uppercase">Wage bill</div>
          <div className="text-gray-300 text-[19px]">${wageBill.toFixed(2)}</div>
        </div>
      </div>

      <div className="mt-[22px]">
        <WeekGrid shifts={SHIFTS} />
      </div>

      <div className="flex gap-[22px] mt-[30px]">
        <div className="w-[37%] border border-gray-300 rounded-none p-[13px] shadow-[3px_3px_0_#999]">
          <div className="text-[17px] text-black mb-[11px]">Open slots</div>
          {openShifts.map(function (s) {
            var urgent = s.day - WEEK.today <= 2;
            return (
              <div
                key={s.id}
                onClick={function () {
                  window.location.hash = "#/shift/" + s.id;
                }}
                className="flex items-center border border-gray-200 px-[11px] py-[9px] mb-[7px] cursor-pointer"
              >
                <span
                  className={"w-[10px] h-[10px] rounded-full mr-[11px] " + (urgent ? "bg-red-500" : "bg-yellow-400")}
                />
                <span className="text-[15px] text-black">
                  {WEEK.days[s.day].short} {s.start}-{s.end}
                </span>
                <span className="text-[15px] text-[#8b8b8b] ml-[9px]">{s.role}</span>
                <span className="ml-auto text-gray-300">
                  <Icon name="chevron" size={15} />
                </span>
              </div>
            );
          })}
        </div>

        <div className="w-[63%] border border-gray-300 rounded-2xl p-[13px] shadow-[0_-4px_12px_rgba(0,0,0,0.25)]">
          <div className="text-[17px] text-black mb-[11px]">Swap requests</div>
          <div className="flex items-center gap-[9px] border border-gray-200 p-[9px]">
            <select className="border border-gray-300 text-[14px] px-[7px] py-[6px] outline-none">
              <option>All statuses</option>
              <option>Pending</option>
              <option>Approved</option>
              <option>Declined</option>
            </select>
            <select className="border border-gray-300 text-[14px] px-[7px] py-[6px] outline-none">
              <option>All roles</option>
              {ROLES.map(function (r) {
                return <option key={r}>{r}</option>;
              })}
            </select>
            <input
              className="border border-gray-300 text-[14px] px-[7px] py-[6px] w-[130px] outline-none"
              placeholder="From DD/MM/YYYY"
            />
            <input
              className="border border-gray-300 text-[14px] px-[7px] py-[6px] w-[130px] outline-none"
              placeholder="To DD/MM/YYYY"
            />
            <button className="bg-[#2f6fed] text-white text-[14px] px-[13px] py-[6px] rounded outline-none">Go</button>
          </div>
          <div className="text-center text-[15px] text-gray-400 py-[38px]">No data</div>
        </div>
      </div>

      <div className="mt-[34px] text-[11px] text-gray-300">
        Unfilled: {openShifts.length} | Projected overtime: ${overtimeCost().toFixed(2)} | Rota v3.2.1
      </div>
    </div>
  );
}
