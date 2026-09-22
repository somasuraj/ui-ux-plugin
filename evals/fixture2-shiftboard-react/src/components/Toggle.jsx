function Toggle({ on, onChange }) {
  return (
    <div
      onClick={function () {
        onChange(!on);
      }}
      className={
        "w-[42px] h-[22px] rounded-full p-[2px] cursor-pointer " + (on ? "bg-green-500" : "bg-gray-300")
      }
    >
      <div
        className={
          "w-[18px] h-[18px] bg-white rounded-full transition-transform " +
          (on ? "translate-x-[20px]" : "translate-x-0")
        }
      />
    </div>
  );
}
