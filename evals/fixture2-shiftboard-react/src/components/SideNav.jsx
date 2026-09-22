var NAV_ITEMS = [
  { key: "schedule", label: "The Grid", icon: "grid", hash: "#/schedule" },
  { key: "team", label: "Crew HQ", icon: "people", hash: "#/team" },
  { key: "settings", label: "Control Room", icon: "sliders", hash: "#/settings" },
];

function SideNav({ current }) {
  return (
    <div className="w-[18%] bg-[#1f2937] pt-[22px] px-[14px]">
      <div className="text-[11px] uppercase text-gray-500 mb-[10px] px-[10px]">Workspace</div>
      {NAV_ITEMS.map(function (item) {
        var active = current === item.key;
        return (
          <div
            key={item.key}
            onClick={function () {
              window.location.hash = item.hash;
            }}
            className={
              "flex items-center gap-[10px] px-[10px] py-[9px] text-[15px] cursor-pointer " +
              (active ? "text-gray-300" : "text-gray-400")
            }
          >
            <Icon name={item.icon} size={17} />
            {item.label}
          </div>
        );
      })}
      <div className="text-[11px] uppercase text-gray-500 mt-[26px] mb-[10px] px-[10px]">Locations</div>
      {OTHER_LOCATIONS.map(function (name) {
        return (
          <div key={name} className="px-[10px] py-[7px] text-[14px] text-gray-400 cursor-pointer">
            {name}
          </div>
        );
      })}
    </div>
  );
}
