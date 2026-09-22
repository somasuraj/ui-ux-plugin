function WeekGridCell({ shift }) {
  var person = shift.staffId ? staffById(shift.staffId) : null;
  var base =
    "block rounded px-1.5 py-1 text-xs leading-tight font-normal focus:outline-none focus-visible:ring-2 focus-visible:ring-brand-500 ";
  var tone = person
    ? "bg-white border border-gray-200 text-ink-900 hover:border-brand-500"
    : "bg-amber-50 border border-dashed border-amber-400 text-amber-900 hover:bg-amber-100";
  return (
    <a href={"#/shift/" + shift.id} className={base + tone}>
      <div className="font-medium tabular-nums">
        {shift.start}-{shift.end}
      </div>
      <div className="truncate">{person ? shortName(person.name) : "Open - unassigned"}</div>
      <div className="text-ink-500">{shift.role}</div>
    </a>
  );
}

function WeekGrid({ shifts }) {
  return (
    <div className="grid grid-cols-7 gap-px bg-gray-200 border border-gray-200 rounded-card overflow-hidden">
      {WEEK.days.map(function (day) {
        var dayShifts = shifts
          .filter(function (s) {
            return s.day === day.key;
          })
          .sort(function (a, b) {
            return toMinutes(a.start) - toMinutes(b.start);
          });
        var isToday = day.key === WEEK.today;
        return (
          <div key={day.key} className="bg-surface min-h-[220px]">
            <div
              className={
                "px-2 py-1.5 text-xs font-semibold border-b border-gray-200 " +
                (isToday ? "bg-brand-50 text-brand-700" : "bg-white text-ink-700")
              }
            >
              {day.short} {day.date}
              {isToday ? " - Today" : ""}
            </div>
            <div className="p-1 space-y-1">
              {dayShifts.map(function (s) {
                return <WeekGridCell key={s.id} shift={s} />;
              })}
            </div>
          </div>
        );
      })}
    </div>
  );
}
