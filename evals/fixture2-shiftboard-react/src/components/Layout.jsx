function Layout({ current, children }) {
  return (
    <div className="min-w-[1240px] min-h-screen flex flex-col font-sans font-light text-black bg-white">
      <TopBar />
      <div className="flex flex-1">
        <SideNav current={current} />
        <div className="w-[82%] px-[22px] py-[26px]">{children}</div>
      </div>
    </div>
  );
}
