class config:
    BOT_TOKEN = ""
    APP_ID = ""
    API_HASH = ""
    DATABASE_URL = ""
    SUDO_USERS = "" # Sepearted by space.
    SUPPORT_CHAT_LINK = ""
    DOWNLOAD_DIRECTORY = "./downloads/"
    G_DRIVE_CLIENT_ID = ""
    G_DRIVE_CLIENT_SECRET = ""


class BotCommands:
  Download = ['download', 'dl']
  Authorize = ['auth', 'authorize']
  SetFolder = ['setfolder', 'setfl']
  Revoke = ['revoke']
  Clone = ['copy', 'clone']
  Delete = ['delete', 'del']
  EmptyTrash = ['emptyTrash']
  YtDl = ['ytdl']

class Messages:
    START_MSG = "**مرحبا عزيزي {}.**\nأنا Google Drive Uploader Bot يمكنك استخدامه لتحميل أي ملف / فيديو إلى Google Drive من رابط مباشر أو ملفات Telegram.\nلمعرفة كيف استخدام البوت اضغط  /help.__"

    HELP_MSG = [
        ".",
        "**Google Drive Uploader**\nيمكنني تحميل الملفات من رابط مباشر أو ملفات Telegram إلى Google Drive الخاص بك. كل ما أحتاجه هو ربط البوت  على حساب Google Drive الخاص بك وإرسال رابط تنزيل مباشر أو ملف Telegram.\n\nلدي ايضا المزيد من المميزات ... !هل تريد ان تكتشف ذلك  ? فقط تابع الخطوات التوضيحية التالية بعناية .",
        
        f"**ربط البوت بحساب قوقل درايف **\nارسل  الامر  /{BotCommands.Authorize[0]} وسوف تحصل على رابط المصادقة , ادخل على الرابط بالزر بالاسفل واتبع كل الخطوات وقم بنسخ الكود الذي سوف تحصل عليه وارسله الى هنا . استخدم الامر  /{BotCommands.Revoke[0]}  لتسجيل الخروج من قوقل درايف باي وقت تريد ذلك.__\n\n**ملاحظة : انا لا افهم ولا استجيب لاي امر الا فقط   الامر ( /{BotCommands.Authorize[0]} ) حتى تقوم بربط البوت بحساب قوقل درايف  .\nلذلك ربط البوت بحساب قوقل درايف اجباري كي اعمل بشكل صحيح !**",
        
        f"**تحميل الروابط المباشرة **\n يمكنك ايضا ارسال رابط مباشر لاي ملف وانا ساقوم بتحميله للسيرفر الخاص بالبوت ثم ارفعه الى حسابك بقوقل درايف .تستطيع ايضا اعادة تسمية الملفات قبل رفعها لقوقل درايف  . فقط ارسل لي رابط التحميل المباشر ثم  علامة  ' | ' ثم الاسم الجديد للملف .__\n\n**مثال ذلك :**\n```https://example.com/AFileWithDirectDownloadLink.mkv | اسم-الملف.mkv```\n\n**ملفات تلقرام **\nلرفع  ملفات telegram الى  حساب Google Drive الخاص بك ، ما عليك سوى إرسال الملف إلي وسأقوم بتنزيله وتحميله إلى حساب Google Drive الخاص بك. ملاحظة : تنزيل ملفات Telegram بطيء. قد يستغرق الأمر وقتًا أطول للملفات الكبيرة.__\n\n**البوت ايضا يدعم تحميل فديوهات اليوتيوب**\nلتحميل فديوهات يوتيوب ورفعها الى قوقل درايف .\nاستخدم الامر  مثال ذلك :  /{BotCommands.Ytdl[0]} رابط اليوتيوب ",
        
        f"**تعيين مجلد معين **\nهل ترغب ان ترفع الملفات الى مجلد معين ا الى  **TeamDrive**  ?\n استخدم الامر ( /{BotCommands.SetFolder[0]} رابط المجلد ) لتخصيص مجلد معين .\nكل الملفات سوف ارفعها الى المجلد المعين الذي قمت بتخصيصه .",
        
        f"**حذف ملفات Google Drive **\n لحذف اي ملف او اي مجلد  بقوقل درايف . استخدم الامر ( /{BotCommands.Delete[0]} رابط المجلد / رابط الملف) .\nيمكنك ايضا تفريغ سلة المهملات  باستخدام  الامر  /{BotCommands.EmptyTrash[0]}\nملاحظة : الملفات ستحذف بشكل نهائي . هذه العملية لا يمكن الغاؤها .\n\n**نسخ ملفات  Google Drive **\nنعم استنساخ  ونسخ ,ملفات  Google Drive .\n لعمل ذلك استخدم الامر ( /{BotCommands.Clone[0]} ايدي الملف / ايدي المجلد او رابطه ) لاستنساخ اي ملف او مجلد على حسابك ",
        
        "**القواعد  & التحذيرات **\n 1.لا تنسخ ملفات / مجلدات Google Drive الكبيرة. قد يتعطل الروبوت وقد تتلف ملفاتك.\n2. أرسل طلبًا واحدًا في كل مرة  وانتظر حتى يكمل البوت العملية ما لم سيوقف البوت جميع العملياتs.\n3. لا ترسل للبوت روابط بطيئة التحميل .\n4. لا تسيء استخدام هذه الخدمة المجانية أو تفرط في تحميلها أو تسيء استخدامها فيما لا يرضي الله  وفي الاخير شكرا لكم لاستخدامكم البوت الخاص بنا  وتقبلوا خالص تحاياتي  أخوكم المجاهد عدي الغولي.",
        
        # Dont remove this ↓ if you respect developer.
        "**تم تطوير البوت بواسطة  @haidarkrar**"
        ]
     
    RATE_LIMIT_EXCEEDED_MESSAGE = "❗ **لقد تجاوزت الحد اليومي المسموح به .**\nحاول مرة اخرى بعد 24 ساعة .__"
    
    FILE_NOT_FOUND_MESSAGE = "❗ **الملف او المجلد المطلوب  **\_File id - {}  . غير موجود . تاكد بانه صحيح ومتاح بنفس الحساب المربوط بالبوت ."
    
    INVALID_GDRIVE_URL = "❗ **رابط قوقل درايف خاطئ **\nتاكد من ان الرابط بالصيغه الصحيحه ."
    
    COPIED_SUCCESSFULLY = "✅ **تم  النسخ بنجاح .**\n[{}]({}) __({})__"
    
    NOT_AUTH = f"🔑 **المعذرة لم تربطني باي حساب  حتى اقوم برفع الملفات .**\nارسل الامر  /{BotCommands.Authorize[0]} لربط  حساب قوقل درايف ."
    
    DOWNLOADED_SUCCESSFULLY = "📤 **جاري رفع الملف ...**\n**اسم الملف :** ```{}```\n**حجم الملف :** ```{}```"
    
    UPLOADED_SUCCESSFULLY = "✅ **تم رفع الملف بنجاح .**\n[{}]({}) __({})__"
    
    DOWNLOAD_ERROR = "❗**فشل التحميل  **\n{}\n__الرابط  - {}__"
    
    DOWNLOADING = "📥 **جاري  تحميل الملف ...\nالرابط :** ```{}```"
    
    ALREADY_AUTH = "🔒 **البوت مربوط بالفعل بحساب  Google Drive .**\n استخدم الامر  /revoke لتسجيل الخروج من الحساب الحالي .\nأرسل لي رابطًا مباشرًا أو ملفًا للتحميل على Google Drive"
    
    FLOW_IS_NONE = f"❗ **الكود غير صحيح **\n اضغط  {BotCommands.Authorize[0]} اولا ."
    
    AUTH_SUCCESSFULLY = '🔐 **تم ربط حسابك بنجاح .**'
    
    INVALID_AUTH_CODE = '❗ **الكود غير صحيح **\nالرمز الذي أرسلته غير صالح أو تم استخدامه من قبل. قم بإنشاء واحد جديد من خلال عنوان URL الخاص بالمصادقة '
    
    AUTH_TEXT = "⛓️ **لربط البوت بحساب قوقل درايف الخاص بك   [اضغط هنا ]({}) ثم ارسل الكود الى هنا .**\nقم بالدخول للرابط بالاسفل  > اعطي البوت الصلاحيات  > سوف تحصل على كود  >انسخه  > ارسل الكود الى البوت "
    
    DOWNLOAD_TG_FILE = "📥 **جاري تحميل الملف...**\n**اسم الملف :** ```{}```\n**حجم الملف :** ```{}```\n**نوع الملف :** ```{}```"
    
    PARENT_SET_SUCCESS = '🆔✅ **تم تعيين المجلد بنجاح .**\n ايدي المجلد الحالي هو  - {}\n استخدم  الامر  ```/{} clear``` لمسحه وتعيين المجلد الافتراضي '
    
    PARENT_CLEAR_SUCCESS = f'🆔🚮 **تم استعادة الملف الافتراضي بنجاح .**\n يمكنك باي وقت استخدام الامر  ``` ( /{BotCommands.SetFolder[0]} رابط المجلد )``` لتعيين مجلد مجددا .'
    
    CURRENT_PARENT = "🆔 **اي المجلد الحالي هو  - {}**\nاستخدم  الامر  ```( /{} رابط المجلد )``` لتغييرة "
    
    REVOKED = f"🔓 **تم تسجيل الخروج من الحساب بنجاح .**\n بامكانك باي وقت استخدام الامر  /{BotCommands.Authorize[0]} لربط حسابك بالبوت مجددا ."
    
    NOT_FOLDER_LINK = "❗ **رابط  ملف غير صحيح .**\nالرابط الذي ارسلته عباره عن رابط مجلد ."
    
    CLONING = "🗂️ **جاري  الاستنساخ في قوقل درايف ...**\nالرابط    - {}__"
    
    PROVIDE_GDRIVE_URL = "**❗ أدخل عنوان URL صالحًا لـ Google Drive مع الأمر .**\nاستخدم  - ( /{} رابط قوقل درايف )__"
    
    INSUFFICIENT_PERMISSONS = "❗ **ليس لديك صلاحيات  كافية لهذا الملف.**\nرابط الملف  - {}"
    
    DELETED_SUCCESSFULLY = "🗑️✅ *تم حذف الملف بنجاح .**\nتم الحذف بشكل نهائي  !\nايدي الملف  - {}"
    
    WENT_WRONG = "⁉️ **خطأ: لقد حدث خطأ **\nالرجاء المحاولة لاحقا ."
    
    EMPTY_TRASH = "🗑️🚮**تم تفريغ سلة المهملات بنجاح  !**"
    
    PROVIDE_YTDL_LINK = "❗**الرجاء ارسال رابط يوتيوب .**"
