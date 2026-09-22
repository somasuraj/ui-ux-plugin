var STATUS_DOT = {
  active: "bg-green-500",
  new: "bg-blue-500",
  leave: "bg-orange-400",
};

function Team() {
  var queryState = React.useState("");
  var query = queryState[0];
  var setQuery = queryState[1];

  var people = STAFF.filter(function (p) {
    var q = query.trim().toLowerCase();
    return q === "" || p.name.toLowerCase().indexOf(q) !== -1 || p.role.toLowerCase().indexOf(q) !== -1;
  });

  return (
    <div>
      <div className="flex items-end justify-between">
        <div>
          <label htmlFor="team-search" className="block text-sm font-medium text-ink-700 mb-1">
            Search staff
          </label>
          <input
            id="team-search"
            type="search"
            value={query}
            onChange={function (e) {
              setQuery(e.target.value);
            }}
            placeholder="Name or role"
            className="w-72 rounded-md border border-gray-300 px-3 py-2 text-sm font-normal text-ink-900 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-brand-500 focus:border-brand-500"
          />
        </div>
        <button className="bg-blue-600 text-white text-[15px] px-[17px] py-[9px] rounded-2xl outline-none">
          Add
        </button>
      </div>

      <table className="w-[1100px] mt-[22px] border border-gray-300 border-collapse">
        <thead>
          <tr>
            {["", "Name", "Role", "Rotas", "Hours", "Contracted", "Rate", "Cost", "Contact", ""].map(function (h, i) {
              return (
                <th
                  key={i}
                  className="border border-gray-300 text-left text-[15px] font-normal uppercase text-black px-[9px] py-[9px]"
                >
                  {h}
                </th>
              );
            })}
          </tr>
        </thead>
        <tbody>
          {people.map(function (p) {
            var hours = hoursFor(p.id);
            return (
              <tr key={p.id}>
                <td className="border border-gray-300 px-[9px] py-[9px]">
                  <img src={avatarFor(p)} className="w-[32px] h-[32px] rounded-full" />
                </td>
                <td className="border border-gray-300 text-[15px] text-black px-[9px] py-[9px]">
                  <span className={"inline-block w-[9px] h-[9px] rounded-full mr-[7px] " + STATUS_DOT[p.status]} />
                  {p.name}
                </td>
                <td className="border border-gray-300 text-[15px] text-black px-[9px] py-[9px]">{p.role}</td>
                <td className="border border-gray-300 text-[15px] text-black text-left px-[9px] py-[9px]">
                  {shiftCountFor(p.id)}
                </td>
                <td className="border border-gray-300 text-[15px] text-black text-left px-[9px] py-[9px]">
                  {hours.toFixed(1)}
                </td>
                <td className="border border-gray-300 text-[15px] text-black text-left px-[9px] py-[9px]">
                  {p.contracted}
                </td>
                <td className="border border-gray-300 text-[15px] text-black text-left px-[9px] py-[9px]">
                  ${p.rate.toFixed(2)}
                </td>
                <td className="border border-gray-300 text-[15px] text-black text-left px-[9px] py-[9px]">
                  ${(hours * p.rate).toFixed(2)}
                </td>
                <td className="border border-gray-300 text-[15px] text-black px-[9px] py-[9px]">
                  {p.email}
                  <br />
                  {p.phone}
                </td>
                <td className="border border-gray-300 px-[9px] py-[9px] whitespace-nowrap">
                  <button className="bg-blue-600 text-white text-[13px] px-[11px] py-[5px] rounded mr-[5px] outline-none">
                    Edit
                  </button>
                  <button className="bg-green-600 text-white text-[13px] px-[11px] py-[5px] rounded mr-[5px] outline-none">
                    Message
                  </button>
                  <button className="bg-red-600 text-white text-[13px] px-[11px] py-[5px] rounded outline-none">
                    Remove
                  </button>
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>

      <section aria-labelledby="timeoff-heading" className="mt-10 max-w-xl">
        <h2 id="timeoff-heading" className="text-lg font-semibold text-ink-900">
          Time off requests
        </h2>
        <div className="mt-3 rounded-card border border-dashed border-gray-300 bg-surface px-6 py-8">
          <p className="text-base font-medium text-ink-900">No time off requests this week</p>
          <p className="mt-1 text-sm font-normal text-ink-700">
            When someone asks for a day off it shows up here so you can approve it before you publish the schedule.
          </p>
          <button className="mt-4 rounded-md bg-brand-600 px-4 py-2 text-sm font-medium text-white hover:bg-brand-700 focus:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-brand-500">
            Add time off for someone
          </button>
        </div>
      </section>
    </div>
  );
}
