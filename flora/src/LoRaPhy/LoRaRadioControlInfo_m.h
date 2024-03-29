//
// Generated file, do not edit! Created by opp_msgtool 6.0 from LoRaPhy/LoRaRadioControlInfo.msg.
//

#ifndef __FLORA_LORARADIOCONTROLINFO_M_H
#define __FLORA_LORARADIOCONTROLINFO_M_H

#if defined(__clang__)
#  pragma clang diagnostic ignored "-Wreserved-id-macro"
#endif
#include <omnetpp.h>

// opp_msgtool version check
#define MSGC_VERSION 0x0600
#if (MSGC_VERSION!=OMNETPP_VERSION)
#    error Version mismatch! Probably this file was generated by an earlier version of opp_msgtool: 'make clean' should help.
#endif


namespace flora {

class LoRaConfigureRadioCommand;
class LoRaTransmissionRequest;
class LoRaReceptionIndication;

}  // namespace flora

#include "inet/common/INETDefs_m.h" // import inet.common.INETDefs

#include "inet/common/packet/chunk/Chunk_m.h" // import inet.common.packet.chunk.Chunk

#include "inet/common/Units_m.h" // import inet.common.Units

// cplusplus {{
using namespace inet;
// }}


namespace flora {

/**
 * Enum generated from <tt>LoRaPhy/LoRaRadioControlInfo.msg:35</tt> by opp_msgtool.
 * <pre>
 * //
 * // Message kinds for sending commands to the radio.
 * //
 * enum LoRaRadioCommandCode
 * {
 *     LORA_RADIO_C_CONFIGURE = 1;
 * }
 * </pre>
 */
enum LoRaRadioCommandCode {
    LORA_RADIO_C_CONFIGURE = 1
};

inline void doParsimPacking(omnetpp::cCommBuffer *b, const LoRaRadioCommandCode& e) { b->pack(static_cast<int>(e)); }
inline void doParsimUnpacking(omnetpp::cCommBuffer *b, LoRaRadioCommandCode& e) { int n; b->unpack(n); e = static_cast<LoRaRadioCommandCode>(n); }

/**
 * Class generated from <tt>LoRaPhy/LoRaRadioControlInfo.msg:43</tt> by opp_msgtool.
 * <pre>
 * //
 * // Control info attached to a configure command that is sent to the ~Radio.
 * //
 * class LoRaConfigureRadioCommand
 * {
 *     int radioMode = -1;                  // new radio mode or -1 if not set.
 *     inet::W power;                    // new default transmission power in the range (0, +infinity) or NaN if not set.
 *     inet::bps bitrate;              // new default bitrate in the range (0, +infinity) or NaN if not set.
 *     //IModulationPtr modulation = nullptr; // new default modulation or nullptr if not set.
 *     inet::Hz carrierFrequency;       // new default carrier frequency in the range (0, +infinity) or NaN if not set.
 *     inet::Hz bandwidth;              // new default bandwidth in the rage (0, +infinity) or NaN if not set.
 * }
 * </pre>
 */
class LoRaConfigureRadioCommand
{
  protected:
    int radioMode = -1;
    ::inet::W power = W(NaN);
    ::inet::bps bitrate = bps(NaN);
    ::inet::Hz carrierFrequency = Hz(NaN);
    ::inet::Hz bandwidth = Hz(NaN);

  private:
    void copy(const LoRaConfigureRadioCommand& other);

  protected:
    bool operator==(const LoRaConfigureRadioCommand&) = delete;

  public:
    LoRaConfigureRadioCommand();
    LoRaConfigureRadioCommand(const LoRaConfigureRadioCommand& other);
    virtual ~LoRaConfigureRadioCommand();
    LoRaConfigureRadioCommand& operator=(const LoRaConfigureRadioCommand& other);
    virtual void parsimPack(omnetpp::cCommBuffer *b) const;
    virtual void parsimUnpack(omnetpp::cCommBuffer *b);

    virtual int getRadioMode() const;
    virtual void setRadioMode(int radioMode);

    virtual ::inet::W getPower() const;
    virtual void setPower(::inet::W power);

    virtual ::inet::bps getBitrate() const;
    virtual void setBitrate(::inet::bps bitrate);

    virtual ::inet::Hz getCarrierFrequency() const;
    virtual void setCarrierFrequency(::inet::Hz carrierFrequency);

    virtual ::inet::Hz getBandwidth() const;
    virtual void setBandwidth(::inet::Hz bandwidth);
};

/**
 * Class generated from <tt>LoRaPhy/LoRaRadioControlInfo.msg:56</tt> by opp_msgtool.
 * <pre>
 * //
 * // Control info attached to a mac frame that is sent down to the ~Radio.
 * //
 * class LoRaTransmissionRequest
 * {
 *     inet::W power;              // override default transmission power in the range (0, +infinity) or NaN if not set.
 *     inet::bps bitrate;        // override default bitrate in the range (0, +infinity) or NaN if not set.
 *     inet::Hz carrierFrequency; // override default carrier frequency in the range (0, +infinity) or NaN if not set.
 *     inet::Hz bandwidth;        // override default bandwidth in the rage (0, +infinity) or NaN if not set.
 * }
 * </pre>
 */
class LoRaTransmissionRequest
{
  protected:
    ::inet::W power = W(NaN);
    ::inet::bps bitrate = bps(NaN);
    ::inet::Hz carrierFrequency = Hz(NaN);
    ::inet::Hz bandwidth = Hz(NaN);

  private:
    void copy(const LoRaTransmissionRequest& other);

  protected:
    bool operator==(const LoRaTransmissionRequest&) = delete;

  public:
    LoRaTransmissionRequest();
    LoRaTransmissionRequest(const LoRaTransmissionRequest& other);
    virtual ~LoRaTransmissionRequest();
    LoRaTransmissionRequest& operator=(const LoRaTransmissionRequest& other);
    virtual void parsimPack(omnetpp::cCommBuffer *b) const;
    virtual void parsimUnpack(omnetpp::cCommBuffer *b);

    virtual ::inet::W getPower() const;
    virtual void setPower(::inet::W power);

    virtual ::inet::bps getBitrate() const;
    virtual void setBitrate(::inet::bps bitrate);

    virtual ::inet::Hz getCarrierFrequency() const;
    virtual void setCarrierFrequency(::inet::Hz carrierFrequency);

    virtual ::inet::Hz getBandwidth() const;
    virtual void setBandwidth(::inet::Hz bandwidth);
};

/**
 * Class generated from <tt>LoRaPhy/LoRaRadioControlInfo.msg:67</tt> by opp_msgtool.
 * <pre>
 * //
 * // Control info attached to a mac frame that is sent up from the ~Radio.
 * //
 * class LoRaReceptionIndication
 * {
 *     //int bitErrorCount = -1;       // number of erroneous bits in the range [0, +infinity) or -1 if unknown.
 *     //int symbolErrorCount = -1;    // number of erroneous symbols in the range [0, +infinity) or -1 if unknown.
 *     //double packetErrorRate = NaN; // packet error rate (probability) in the range [0, 1] or NaN if unknown.
 *     //double bitErrorRate = NaN;    // bit error rate (probability) in the range [0, 1] or NaN if unknown.
 *     //double symbolErrorRate = NaN; // symbol error rate (probability) in the range [0, 1] or NaN if unknown.
 *     inet::W minRSSI;           // minimum receive signal strength indication in the range (0, +infinity) or NaN if unknown.
 *     double minSNIR;         // minimum signal to noise plus interference ratio in the range (0, +infinity) or NaN if unknown.
 *     inet::W LoRaTP;
 *     inet::Hz LoRaCF;
 *     int LoRaSF;
 *     inet::Hz LoRaBW;
 *     int LoRaCR;
 * }
 * </pre>
 */
class LoRaReceptionIndication
{
  protected:
    ::inet::W minRSSI = W(NaN);
    double minSNIR = 0;
    ::inet::W LoRaTP = W(NaN);
    ::inet::Hz LoRaCF = Hz(NaN);
    int LoRaSF = 0;
    ::inet::Hz LoRaBW = Hz(NaN);
    int LoRaCR = 0;

  private:
    void copy(const LoRaReceptionIndication& other);

  protected:
    bool operator==(const LoRaReceptionIndication&) = delete;

  public:
    LoRaReceptionIndication();
    LoRaReceptionIndication(const LoRaReceptionIndication& other);
    virtual ~LoRaReceptionIndication();
    LoRaReceptionIndication& operator=(const LoRaReceptionIndication& other);
    virtual void parsimPack(omnetpp::cCommBuffer *b) const;
    virtual void parsimUnpack(omnetpp::cCommBuffer *b);

    virtual ::inet::W getMinRSSI() const;
    virtual void setMinRSSI(::inet::W minRSSI);

    virtual double getMinSNIR() const;
    virtual void setMinSNIR(double minSNIR);

    virtual ::inet::W getLoRaTP() const;
    virtual void setLoRaTP(::inet::W LoRaTP);

    virtual ::inet::Hz getLoRaCF() const;
    virtual void setLoRaCF(::inet::Hz LoRaCF);

    virtual int getLoRaSF() const;
    virtual void setLoRaSF(int LoRaSF);

    virtual ::inet::Hz getLoRaBW() const;
    virtual void setLoRaBW(::inet::Hz LoRaBW);

    virtual int getLoRaCR() const;
    virtual void setLoRaCR(int LoRaCR);
};


}  // namespace flora


namespace omnetpp {

inline any_ptr toAnyPtr(const flora::LoRaConfigureRadioCommand *p) {if (auto obj = as_cObject(p)) return any_ptr(obj); else return any_ptr(p);}
template<> inline flora::LoRaConfigureRadioCommand *fromAnyPtr(any_ptr ptr) { return ptr.get<flora::LoRaConfigureRadioCommand>(); }
inline any_ptr toAnyPtr(const flora::LoRaTransmissionRequest *p) {if (auto obj = as_cObject(p)) return any_ptr(obj); else return any_ptr(p);}
template<> inline flora::LoRaTransmissionRequest *fromAnyPtr(any_ptr ptr) { return ptr.get<flora::LoRaTransmissionRequest>(); }
inline any_ptr toAnyPtr(const flora::LoRaReceptionIndication *p) {if (auto obj = as_cObject(p)) return any_ptr(obj); else return any_ptr(p);}
template<> inline flora::LoRaReceptionIndication *fromAnyPtr(any_ptr ptr) { return ptr.get<flora::LoRaReceptionIndication>(); }

}  // namespace omnetpp

#endif // ifndef __FLORA_LORARADIOCONTROLINFO_M_H

