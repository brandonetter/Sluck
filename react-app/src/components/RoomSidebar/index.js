import { useDispatch } from "react-redux";
import { joinDefaultRoom } from "../../store/channel";
import { useEffect, useState } from "react";
import { useSelector } from "react-redux";
import "./RoomSidebar.css";
import { getChannel } from "../../store/channels";
import GroupDM from "../GroupDM";
import Channels from "../Channels";
// import Modal from "../ChannelModal/ChannelModal";
// import ChannelList "../ChannelList"

function RoomSidebar() {
  const dispatch = useDispatch();
  const currentChannel = useSelector((state) => state.channel.room);
  useEffect(() => {
    if (!currentChannel) dispatch(joinDefaultRoom());
  }, []);
  // const [modalOpen, setModalOpen] = useState(false);
  const channels = useSelector((state) => state.channels)

  const dms = useSelector((state) => state.dms)
  return (
    <div className="room-sidebar">
      <div className="room-sidebar-header">

        <Channels />
        <GroupDM />


      </div>
    </div>
  );
}
export default RoomSidebar;
