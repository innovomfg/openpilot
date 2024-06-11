#pragma once

#include <cassert>
#include <cstdint>
#include <memory>
#include <thread>
#include <vector>

#include "cereal/messaging/messaging.h"
<<<<<<< HEAD
#include "msgq/visionipc/visionipc.h"
=======
#include "cereal/visionipc/visionipc.h"
>>>>>>> 8b9791041 (sunnypilot v2024.06.11-2039)
#include "common/queue.h"
#include "system/camerad/cameras/camera_common.h"
#include "system/loggerd/loggerd.h"

#define V4L2_BUF_FLAG_KEYFRAME 8

class VideoEncoder {
public:
  VideoEncoder(const EncoderInfo &encoder_info, int in_width, int in_height);
  virtual ~VideoEncoder() {}
  virtual int encode_frame(VisionBuf* buf, VisionIpcBufExtra *extra) = 0;
  virtual void encoder_open(const char* path) = 0;
  virtual void encoder_close() = 0;

  void publisher_publish(VideoEncoder *e, int segment_num, uint32_t idx, VisionIpcBufExtra &extra, unsigned int flags, kj::ArrayPtr<capnp::byte> header, kj::ArrayPtr<capnp::byte> dat);

protected:
  void publish_thumbnail(uint32_t frame_id, uint64_t timestamp_eof, kj::ArrayPtr<capnp::byte> dat);

  int in_width, in_height;
  int out_width, out_height;
  const EncoderInfo encoder_info;

private:
  // total frames encoded
  int cnt = 0;
  std::unique_ptr<PubMaster> pm;
  std::vector<capnp::byte> msg_cache;
};
