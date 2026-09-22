function TopBarIcon({ name, onClick }) {
  return (
    <button
      onClick={onClick}
      className="w-[34px] h-[34px] flex items-center justify-center rounded-full text-white opacity-60 hover:opacity-100 outline-none"
    >
      <Icon name={name} size={19} />
    </button>
  );
}

function TopBar() {
  var me = staffById(1);
  return (
    <div className="h-[58px] bg-[#2f6fed] flex items-center px-[18px] shadow-[0_3px_9px_rgba(0,0,0,0.35)]">
      <div className="text-white/50 text-[13px]">
        {LOCATION.name} | Week {WEEK.number}
      </div>
      <div className="flex items-center ml-[26px] gap-[6px]">
        <TopBarIcon name="help" />
        <TopBarIcon name="gift" />
        <TopBarIcon name="chat" />
        <TopBarIcon name="apps" />
        <TopBarIcon name="bell" />
        <TopBarIcon name="mail" />
        <TopBarIcon name="moon" />
        <span className="text-white/60 text-[13px] ml-[10px] cursor-pointer">Invite</span>
        <span className="text-white/60 text-[13px] ml-[14px] cursor-pointer">Refer a cafe</span>
        <span className="text-[#15306b] bg-yellow-300 text-[12px] px-[9px] py-[3px] rounded-full ml-[14px] cursor-pointer">
          Upgrade
        </span>
      </div>
      <div className="ml-auto flex items-center">
        <img src={avatarFor(me)} className="w-[30px] h-[30px] rounded-full mr-[22px]" />
        <img src={LOGO_SRC} className="w-[26px] h-[26px]" />
        <div className="text-white text-[19px] ml-[8px]">Shiftboard</div>
      </div>
    </div>
  );
}
